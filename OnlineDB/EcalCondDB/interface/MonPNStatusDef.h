#ifndef MONPNSTATUSDEF_H
#define MONPNSTATUSDEF_H

#include <string>
#include <stdexcept>

#include "OnlineDB/EcalCondDB/interface/IDef.h"

/**
 *   Def for monitoring run outcomes
 */
class MonPNStatusDef : public IDef {
  public:
  friend class EcalCondDBInterface;
  
  MonPNStatusDef();
  virtual ~MonPNStatusDef();

  // Methods for user data
  std::string getShortDesc() const;
  void setShortDesc(std::string desc);

  std::string getLongDesc() const;

  // Methods from IUniqueDBObject
  int fetchID() throw(std::runtime_error);
  void setByID(int id) throw(std::runtime_error);

 protected:
  // User data for this def
  std::string m_shortDesc;
  std::string m_longDesc;

  void fetchAllDefs( std::vector<MonPNStatusDef>* fillVec) throw(std::runtime_error);
};

#endif
