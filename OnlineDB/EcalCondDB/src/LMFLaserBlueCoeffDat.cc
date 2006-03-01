#include <stdexcept>
#include <string>
#include "occi.h"

#include "OnlineDB/EcalCondDB/interface/LMFLaserBlueCoeffDat.h"
#include "OnlineDB/EcalCondDB/interface/RunTag.h"
#include "OnlineDB/EcalCondDB/interface/RunIOV.h"

using namespace std;
using namespace oracle::occi;

LMFLaserBlueCoeffDat::LMFLaserBlueCoeffDat()
{
  m_env = NULL;
  m_conn = NULL;
  m_writeStmt = NULL;

  m_xportCoeff = 0;
  m_xportCoeffRMS = 0;
}



LMFLaserBlueCoeffDat::~LMFLaserBlueCoeffDat()
{
}



void LMFLaserBlueCoeffDat::prepareWrite()
  throw(runtime_error)
{
  this->checkConnection();

  try {
    m_writeStmt = m_conn->createStatement();
    m_writeStmt->setSQL("INSERT INTO lmf_laser_blue_coeff_dat (iov_id, logic_id, "
			"xport_coeff, xport_coeff_rms) "
			"VALUES (:iov_id, :logic_id, "
			":3, :4)");
  } catch (SQLException &e) {
    throw(runtime_error("LMFLaserBlueCoeffDat::prepareWrite():  "+e.getMessage()));
  }
}



void LMFLaserBlueCoeffDat::writeDB(const EcalLogicID* ecid, const LMFLaserBlueCoeffDat* item, LMFRunIOV* iov)
  throw(runtime_error)
{
  this->checkConnection();
  this->checkPrepare();

  int iovID = iov->fetchID();
  if (!iovID) { throw(runtime_error("LMFLaserBlueCoeffDat::writeDB:  IOV not in DB")); }

  int logicID = ecid->getLogicID();
  if (!logicID) { throw(runtime_error("LMFLaserBlueCoeffDat::writeDB:  Bad EcalLogicID")); }
  
  try {
    m_writeStmt->setInt(1, iovID);
    m_writeStmt->setInt(2, logicID);

    m_writeStmt->setFloat(3, item->getXportCoeff() );
    m_writeStmt->setFloat(4, item->getXportCoeffRMS() );

    m_writeStmt->executeUpdate();
  } catch (SQLException &e) {
    throw(runtime_error("LMFLaserBlueCoeffDat::writeDB():  "+e.getMessage()));
  }
}



void LMFLaserBlueCoeffDat::fetchData(std::map< EcalLogicID, LMFLaserBlueCoeffDat >* fillMap, LMFRunIOV* iov)
  throw(runtime_error)
{
  this->checkConnection();
  fillMap->clear();

  iov->setConnection(m_env, m_conn);
  int iovID = iov->fetchID();
  if (!iovID) { 
    //  throw(runtime_error("LMFLaserBlueCoeffDat::writeDB:  IOV not in DB")); 
    return;
  }

  try {
    Statement* stmt = m_conn->createStatement();
    stmt->setSQL("SELECT cv.name, cv.logic_id, cv.id1, cv.id2, cv.id3, cv.maps_to, "
		 "d.xport_coeff, d.xport_coeff_rms "
		 "FROM channelview cv JOIN lmf_laser_blue_coeff_dat d "
		 "ON cv.logic_id = d.logic_id AND cv.name = cv.maps_to "
		 "WHERE d.iov_id = :iov_id");
    stmt->setInt(1, iovID);
    ResultSet* rset = stmt->executeQuery();
    
    std::pair< EcalLogicID, LMFLaserBlueCoeffDat > p;
    LMFLaserBlueCoeffDat dat;
    while(rset->next()) {
      p.first = EcalLogicID( rset->getString(1),     // name
			     rset->getInt(2),        // logic_id
			     rset->getInt(3),        // id1
			     rset->getInt(4),        // id2
			     rset->getInt(5),        // id3
			     rset->getString(6));    // maps_to

      dat.setXportCoeff( rset->getFloat(7) );
      dat.setXportCoeffRMS( rset->getFloat(8) );

      p.second = dat;
      fillMap->insert(p);
    }
  } catch (SQLException &e) {
    throw(runtime_error("LMFLaserBlueCoeffDat::fetchData():  "+e.getMessage()));
  }
}
