#!/usr/bin/perl

use warnings;
use strict;

use CondDB::Oracle;

package ConnectionFile;

# connection information
our $host = "pccmsecdb.cern.ch";
our $db = "ecalh4db";
our $user = "test01";
our $pass = "oratest01";
our $db_opts = {RaiseError=>1};

# return the conditions database interface
sub connect {
  my $condDB = new CondDB::Oracle;
  
  $condDB->connect(-host=>$host,
		   -db=>$db,
		   -user=>$user,
		   -pass=>$pass,
		   -db_opts=>$db_opts);
  $condDB->{dbh}->do(qq[ ALTER SESSION SET NLS_DATE_FORMAT='YYYY-MM-DD HH24:MI:SS']);
  $condDB->{ix_tablespace} = "INDX01";
  return $condDB;
}

1;
