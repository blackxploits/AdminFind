#!/usr/bin/python
# c0ded by blackXploits
# Admin finder v1.3 / 1759 admin panel scan /

w  = '\033[0m'
r  = '\033[31m'
g  = '\033[32m'
o  = '\033[33m'
b  = '\033[34m'

import sys
import time
import httplib
import os

os.system("clear")

def slowprint(s):

    for c in s + '\n':

        sys.stdout.write(c)

        sys.stdout.flush()

        time.sleep(8./90)



jembut = "love"

if jembut=="love":

          print r+"        admin finder v1.3       "

          print   "                                 "
          print b+"    ___       __          _       _______           __"
          print b+"   /   | ____/ /___ ___  (_)___  / ____(_)___  ____/ /"
          print b+"  / /| |/ __  / __ `__ \/ / __ \/ /_  / / __ \/ __  / "
          print b+" / ___ / /_/ / / / / / / / / / / __/ / / / / / /_/ /  "
          print b+"/_/  |_\__,_/_/ /_/ /_/_/_/ /_/_/   /_/_/ /_/\__,_/   "
          print b+"                                      "

          slowprint (o+"                c0ded by blackXploits")

          print w+'                                                      '

site = raw_input(">> Target example : www.site.co.li : ")

site = site.replace("http://","")

conn = httplib.HTTPConnection(site)

conn.connect()



pg = {"admin","login.htm","admin1/login.php","admin1/index.php","adminweb/login","adminweblogin","index.php/admin","index.php/administrator","index.php/login","index.php/cms/adminweb","adweb2_cad/","cms/index.php","cms/login.php","cms/admin/login.php","backend/admin/login","backend","backend/user.php","admin1/user.php","/admin1","user1/","user1/login.php","user1/admin.php","user1/user","redaktur","admin/account.php","adm/adm.php","adm/user.php","ketua/admin.php","admin/content.php","admin/aksi.php","user/aksi.php","user/admin","userLogin.php","userlogin.php""userAdmin.php","useradmin","webadmin.php","webadmin/login.php","redakturweb","administrator","adminsekolah","adminlogin","admin1.php","author/admin.php","author","users/","master/login.php","master/admin.php","master/index.php","operator/index.php","operator/admin.php","operator/login.php","operator/user.php","sika/index.php","redaksi/login.php","redaksi/admin.php","redaksi/index.php","terasadmin/login.php","terasadmin/index.php","rahasia/admin.php","rahasia","rahasia/login.php","rahasia/user.php","rahasia/administrator.php""login.html","login/","adm/","admin/","admin/account.html","admin","login.html","admin/login.htm","admin/controlpanel.html","admin/controlpanel.htm","admin/adminLogin.html","admin","adminLogin.htm","admin.htm","admin.html","adminitem","adminitems","administration/","adminLogin/","admin_area/ ","manager/","letmein/","superuser/","/myadmin","access/","sysadm/","superman/","supervisor/","control/","member/","members/ ","user/","cp/","uvpanel/","manage/","management/ ","signin/","admin/index2.php","user/index2.php","user/admin/index2.php","cms/user/index2.php","cms/admin/index2.php","admin/user/index2.php","log-in/ ","log_in/ ","sign_in/ ","sign-in/ ","users/","accounts/","login_userasp","vmailadmin/","globes_admin/","fileadmin/","login_out.php","admin4_colon/","super.php","admin/ vorud.asp","admin_login.php","manager.php","admin/account.asp","admin_area.asp","admin.html ","usr/ ","administr8.php ","SysAdmin2/ ","adminitem.php","login.php ","management/","project-admins/","typo3/","admin.htm","admin","home.asp","vorud.php","admins/","accounts/","super_loginphp","super_indexphp","adminpanel.php","memberadmin/","access.asp","superuserphp","systemadministration/","pagesadminadminlogin.asp","paneladministracionlogin.asp","sign_in.php","super_loginasp","moderator.html","log_in/","autologin.php","ysadmin.asp","supermanasp","adminitems.php","admincp.asp","acceso.php","loginredirect/","auth.php","login.asp","Database_Administration/","webadmin.asp","modelsearchlogin.asp","cmsadmin/","admincplogin.asp","phpSQLiteAdmin/","login_admin/","ServerAdministrator/","adminlogin.asp","letmein.asp","member/","acct_login/","loginsuperasp","manage.asp","sign_in/","LiveUser_Admin/","administratoraccounts/","utility_login/","administrator.php","secure/","administratorlogin.asp","checklogin.asp","admin_arealogin.php","authentication.php","UserLogin/","webadmin/","rcLogin/","sub-login","authenticate.asp","login.html","adminadminlogin.php","ss_vms_admin_sm/","SysAdmin/","secret/","login1php","fileadmin.php","controlpanel.php","members.asp","login1asp","irectadmin/","adminlogin.asp","affiliate.asp","adminhome.php","admin.asp","superuser/","Server.php","cpanel/","cp.php","customer_login/","access.php","administratie/","control.asp","autologin/","wplogin/","administratorlogin.php","adminadminlogin.asp","openvpnadmin/","checklogin.php","admin1.html","siteadmin.php","yonetim.asp","supervise","Loginasp","adminitem/","admincontrolpanel.php","authuser.php","modelsearchlogin.php","uradmin.asp","showlogin/","webmaster.php","letmein.php","adminlogin.php","sign_in.asp","sshadmin/","loginasp","checkadmin.php","letmein/","panel.php","simpleLogin/","control/","login/","moderator/","adminlogin.asp","members/","admin_area.php","logoutphp","account.php","bbadmin/","administr8/","relogin.asp","cmsadmin.asp","member.php","adminadminLogin.html","adminpanel/","supermanagerphp","paneladministracion/","relogin.html","signin.asp","adm_auth.php","ezsqliteadmin/","adm.asp","member.asp","admin1.php","radmind/","login_outasp","admin2.php","admin_area/","sqladmin/","administratorlogin/","adminlogin.php","admincontrolpanel.htm","processlogin.asp","administrators.asp","admincp/","SuperAdmin/","kpanel/","log_in.asp","webadmin.php","accounts.asp","checkuser.php","ccp14admin/","newsadmin/","check.asp","manuallogin/","phpmyadmin/","administrators/","autologin.asp","checkuser.asp","acceso.asp","adminitems.asp","auth.asp","super.asp","login_user.php","PSUser/","siteadmin.asp","admin_arealogin.asp","wizmysqladmin/","memberadmin.php","userlogin.asp","siteadmin/","adminarea/","adm/","users.php","superviseLoginphp","manager.asp","users.asp","login.htm","cmsadmin.php","administration.asp","signin/","admin_areaadmin.php","admincontrol.asp","supervise/","adminpanel.asp","super1asp","login_adminphp","webmaster/","signin/","bbadmin/","authadmin.asp","adminadminLogin.asp ","hpwebjetadmin/","super1/","support_login/","login_out/","yonetici.html","administratorlogin.asp","bbadminlogin.php","management.php","administer/","yonetici.php","sysadmin/","Lotus_Domino_Admin/","members.php","administrivia/","authenticate.php","banneradmin/","user/ ","AdminTools/ ","admin/controlpanel.html ","webmaster.asp ","administrator.asp ","authuser.asp ","cadmins/","superman/","admincontrol/","bb-admin/admin.php","supervisor/","pgadmin/","loginerror/","admin/admin_login.php","isadmin.asp","check.php","admin/admin_login.asp","admin_area/admin.asp","user.php","admin/admin.php","admin/login.html","admin2.html","admin1/","vorud/","memberadmin.asp","administrator/account.asp""wp-login.php","bbadminadmin.html","relogin.htm","relogin.html","registration/","moderator/","controlpanel/","fileadmin/","admin1.html","admin1.htm","admin2.html","yonetim.html","yonetici.html","phpmyadmin/","myadmin/","uradminServer/","wpadmin/","administr8/","webadmin/","administratie/","admins/","administrivia/","Database_Administration/","useradmin/","sysadmins/","admin1/","systema/dministration/","administrators/","pgadmin ","directadmin/","staradmin/","Server/Administrator/","SysAdmin/","administer","LiveUser_Admin/ ","sysadmin/","typo3/","panel/","cpanel/","cpanel_file/","platz_login/","rcLogin","blogindex/","formslogin/","autologin/","support_login/","meta_login/","manuallogin/","simpleLogin/ ","loginflat/ ","utility_login/ ","showlogin/ ","memlogin/ ","login-redirect/ ","sub-login/","wp-login/ ","login1/ ","dir-login/ ","login_db/ ","xlogin/ ","smblogin/ ","customer_login/ ","UserLogin/ ","login-us/ ","acct_login/ ","bigadmin/ ","project-admins/ ","phppgadmin/ ","pureadmin/ ","sql-admin/ ","radmind/ ","openvpnadmin/ ","wizmysqladmin/ ","vadmind/","ezsqliteadmin/","hpwebjetadmin/","newsadmin/ ","adminpro/ ","Lotus_Domino_Admin/ ","bbadmin/ ","vmailadmin/ ","Indy_admin/ ","ccp14admin/ ","irc-macadmin/ ","banneradmin/","sshadmin/","phpldapadmin/","macadmin/ ","administratoraccounts/ ","admin4_account/ ","admin4_colon/ ","radmind-1/","Super-Admin/","AdminTools/","cmsadmin/ ","SysAdmin2/ ","globes_admin/ ","cadmins/ ","phpSQLiteAdmin/","navSiteAdmin/ ","server_admin_small/ ","logo_sysadmin/","power_user/","system_administration/","ss_vms_admin_sm/","bbadmin/","paneladministracion/","instadmin/","memberadmin/ ","administratorlogin/ ","pages/admin/","admincp/","adminarea/","admincontrol/","modules/admin/","siteadmin/ ","adminsite/ ","kpanel/","vorod/","vorud/ ","adminpanel/","PSUser/ ","secure/","webmaster/","security/","usr/","root/","secret/","moderator.php","moderator.html","0admin/","0manager/ aadmin/","login_admin/","login_out/","loginerror/","loginok/ ","loginsave/ ","loginsuper/ ","logout/","secrets/","super1/ ","supervise/ ","admin1.php ","admin1.html ","admin2.php ","admin2.html","yonetim.php ","yonetim.html ","yonetici.php ","yonetici.html","adm/ ","admin/","adminaccount.php ","admin/account.html ","admin/index.php ","admin/index.html ","admin/login.php ","admin/login.html ","admin/home.php ","admin/controlpanel.html ","admin/controlpanel.php ","admin.php ","admin.html ","admin/cp.php ","admin/cp.html ","cp.php ","cp.html ","administrator/ ","administrator/index.html ","administrator/index.php ","administrator/login.html ","administrator/login.php ","administrator/account.html ","administrator/account.php ","administrator.php ","administrator.html","login.php ","login.html ","modelsearch/login.php ","moderator.php ","moderator.html ","moderator/login.php","moderatorlogin.html","moderatoradmin.php","moderatoradmin.html","moderator/ ","account.php ","account.html ","controlpanel/ ","controlpanel.php ","controlpanel.html ","admincontrol.php","admincontrol.html ","adminpanel.php ","adminpanel.html ","admin1.asp ","admin2.asp ","yonetim.asp ","yonetici.asp ","admin/account.asp ","admin/index.asp ","admin/login.asp ","admin/home.asp","admincontrolpanel.asp","admin.asp ","admin/cp.asp ","cp.asp ","administrator/index.asp ","administrator/login.asp ","administrator/account.asp ","administrator.asp","login.asp ","modelsearch/login.asp ","moderator.asp","moderator/login.asp ","moderator/admin.asp ","account.asp ","controlpanel.asp ","admincontrol.asp ","adminpanel.asp ","fileadmin/ ","fileadmin.php ","fileadmin.asp ","fileadmin.html ","administration/ ","administration.php ","administration.html ","sysadmin.php ","sysadmin.html ","phpmyadmin/","myadmin/","sysadmin.asp ","sysadmin/","ur-admin.asp ","ur-admin.php ","ur-admin.html ","ur-admin/ ","Server.php ","Server.html ","Server.asp ","Server/ ","wp-admin/","administr8.php ","administr8.html ","administr8/ ","administr8.asp ","webadmin/","webadmin.php","webadmin.asp ","webadmin.html ","administratie/ ","admins/ ","admins.php ","admins.asp ","admins.html ","administrivia/ ","Database_Administration/ ","WebAdmin/ ","useradmin/ ","sysadmins/ ","admin1/ ","system-administration/ ","administrators/ ","pgadmin/","directadmin/","staradmin/","ServerAdministrator/","SysAdmin/","administer/","LiveUser_Admin/","sys","admin/ ","typo3/ ","panel/ ","cpanel/ ","cPanel/ ","cpanel_file/ ","platz_login/ ","rcLogin/ ","blogindex/","formslogin/ ","autologin/ ","support_login/ ","meta_login/ ","manuallogin/ ","simpleLogin/ ","loginflat/ ","utility_login/ ","showlogin/ ","memlogin/ ","members/ ","login-redirect/ ","sub-login/ ","wp-login/ ","login1/ ","dir-login/ ","login_db/ ","xlogin/ ","smblogin/ ","customer_login/ ","UserLogin/ ","login-us/ ","acct_login/ ","admin_area/ ","bigadmin/ ","project-admins/ ","phppgadmin/","pureadmin/","sql-admin/","radmind/","openvpnadmin/ ","wizmysqladmin/","vadmind/","ezsqliteadmin/","hpwebjetadmin/","newsadmin/","adminpro/ ","Lotus_Domino_Admin/","bbadmin/ ","vmailadmin/ ","Indy_admin/ ","ccp14admin/ ","irc-macadmin/","banneradmin/ ","sshadmin/ ","phpldapadmin/ ","macadmin/ ","administratoraccounts/","admin4_account/ ","admin4_colon/ ","radmind-1/ ","Super-Admin/","AdminTools/","cmsadmin/ ","SysAdmin2/ ","globes_admin/ ","cadmins/ ","phpSQLiteAdmin/ ","navSiteAdmin/","server_admin_small/ ","logo_sysadmin/ ","server/ ","database_administration/","power_user/","system_administration/","ss_vms_admin_sm/","adiministrador/","adm/ ","adimin/ ","login/ ","logout/ ","senha/ ","membros/","usuarios/","senhas/","sff/","saff/","donos/","noticias/","not/","painel/","administracao/","key/","edit/ ","config/","funcoes/","sistema/","php/","net/","controle","controles","membro","membros","acesso","senha","usuario","usuarios ","admistrador","adimistrador","painel","root","roots","raiz","login.htm","login.html","login/","adm/","admin/","adminaccount.html","adminlogin.html","adminlogin.htm","admincontrolpanel.html","admincontrolpanel.htm","adminadminLogin.html","adminadminLogin.htm","admin.htm","admin.html","adminitem/","adminitems/","administrator/","administration/","adminLogin/","admin_area/ ","manager/ ","letmein/ ","superuser/ ","access/ ","sysadm/ ","superman/ ","supervisor/ ","control/ ","member/ ","members/ ","user/ ","cp/ ","uvpanel/ ","manage/ ","management/ ","signin/ ","log-in/ ","log_in/","sign_in/ ","sign-in/ ","users/ ","accounts/ ","wp-login.php ","bb-admin/admin.html ","relogin.htm ","relogin.html ","moderator/ ","controlpanel/ ","fileadmin/ ","admin1.html ","admin1.htm ","admin2.html ","yonetim.html ","yonetici.html ","phpmyadmin/ ","myadmin/ ","ur-admin/","Server/","wp-admin/ ","administr8/ ","webadmin/ ","administratie/ ","admins/","administrivia/","Database_Administration/ ","useradmin/ ","sysadmins/ ","admin1/ ","system-administration/ ","administrators/ ","pgadmin/ ","directadmin/ ","staradmin/ ","ServerAdministrator/ ","SysAdmin/ ","administer/ ","LiveUser_Admin/ ","sys-admin/ ","typo3/ ","panel/ ","cpanel/ ","cpanel_file/ ","platz_login/ ","rcLogin/ ","blogindex/ ","formslogin/ ","autologin/ ","support_login/ ","meta_login/ ","manuallogin/ ","simpleLogin/ ","loginflat/ ","utility_login/ ","showlogin/ ","memlogin/ ","login-redirect/ ","sub-login/ ","wp-login/ ","login1/ ","dir-login/ ","login_db/ ","xlogin/ ","smblogin/ ","customer_login/ ","UserLogin/ ","login-us/ ","acct_login/ ","bigadmin/ ","projectadmins/ ","phppgadmin/ ","pureadmin/ ","sql-admin/ ","radmind/ ","openvpnadmin/ ","wizmysqladmin/ ","vadmind/ ","ezsqliteadmin/ ","hpwebjetadmin/ ","newsadmin/ ","adminpro/ ","Lotus_Domino_Admin/ ","bbadmin/ ","vmailadmin/ ","Indy_admin/ ","ccp14admin/ ","irc-macadmin/","banneradmin/","sshadmin/ ","phpldapadmin/","macadmin/ ","administratoraccounts/ ","admin4_account/ ","admin4_colon/ ","radmind-1/","Super-Admin/ ","AdminTools/ ","cmsadmin/ ","SysAdmin2/ ","globes_admin/ ","cadmins/ ","phpSQLiteAdmin/ ","navSiteAdmin/","server_admin_small/ ","logo_sysadmin/","power_user/ ","system_administration/ ","ss_vms_admin_sm/ ","bb-admin/ ","panel-administracion/ ","instadmin/ ","memberadmin/ ","administratorlogin/","adm.php","adm.asp","adm.aspx","admin_login.php","admin_login.asp","admin_login.aspx","panel-administracion/login.php","panel-administracion/login.asp","panel-administracion/login.aspx","pages/admin/admin-login.php","pages/admin/admin-login.asp","pages/admin/admin-login.apsx","pages/admin/ ","acceso.php","acceso.asp","acceso.aspx","admincp/login.php","admincp/login.asp","admincp/login.aspx","admincp/ ","adminarea/ ","admincontrol/ ","affiliate.php","affiliate.asp","affiliate.aspx","adm_auth.php","adm_auth.asp","adm_auth.aspx","memberadmin.php","memberadmin.asp","memberadmin.aspx","administratorlogin.php","administratorlogin.asp","administratorlogin.aspx","modules/admin/","administrators.php","administrators.asp","administrators.aspx","siteadmin/ ","siteadmin.php","siteadmin.asp","siteadmin.aspx","adminsite/ ","kpanel/ ","vorod/ ","vorod.php","vorod.asp","vorod.aspx","vorud/ ","vorud.php","vorud.asp","vorud.aspx","adminpanel/","PSUser/","secure/","webmaster/","webmaster.php","webmaster.asp","webmaster.aspx","autologin.php","autologin.asp","autologin.aspx","userlogin.php","userlogin.asp","userlogin.aspx","admin_area.php","admin_area.asp","admin_area.aspx","cmsadmin.php","cmsadmin.asp","cmsadmin.aspx","security/ ","usr/","root/ ","secret/ ","admin/login.php","admin/login.asp","admin/login.aspx","admin/adminLogin.php","admin/adminLogin.asp","adminadminLogin.aspx","moderator.php ","moderator.html ","moderator/login.php","moderator/login.asp","moderator/login.aspx","moderator/admin.php","moderator/admin.asp","moderator/admin.aspx","yonetici.php","yonetici.asp","yonetici.aspx","0admin/ ","0manager/ ","aadmin/ ","cgi-bin/login.php","cgi-bin/login.asp","cgi-bin/login.aspxlogin1.php","login1.asp","login1.aspx","login_admin/ ","login_admin.php","login_admin.asp","login_admin.aspxlogin_out/ ","login_out.php","login_out.asp","login_out.aspx","login_user.php","login_user.asp","login_user.aspx","loginerror/ ","loginok/ ","loginsave/","loginsuper/ ","loginsuper.php","loginsuper.asp","loginsuper.aspx","login.php","login.aspx","login.asp","logout/ ","logout.php","logout.asp","logout.aspx","secrets/ ","super1/ ","super1.php","super1.aspx","super1.asp","super_index.php","super_index.asp","super_index.aspx","super_login.asp","super_login.php","super_login.aspx","supermanager.php","supermanager.asp","supermanager.aspx","superman.php","superman.asp","superman.aspx","superuser.php","superuser.asp","superuser.aspx","supervise/ ","supervise/Login.php","supervise/Login.asp","superviseLogin.aspx","super.php","super.asp","admin.php ","admin/ ","administrator/ ","moderator/ ","webadmin/ ","adminarea/ ","bb-admin/ ","adminLogin/ ","admin_area/ ","panel-administracion/ ","instadmin/ ","memberadmin/ ","administratorlogin/ ","adm/ ","admin/account.php ","admin/index.php ","admin/login.php ","admin/admin.php ","admin/account.php ","joomla/administrator ","login.php ","admin_area/admin.php ","admin_area/login.php ","siteadmin/login.php ","siteadmin/index.php ","siteadmin/login.html ","admin/account.html ","admin/index.html ","admin/login.html ","admin/admin.html ","admin_area/index.php ","bb-admin/index.php ","bb-admin/login.php ","bb-admin/admin.php ","admin/home.php ","admin_area/login.html ","admin_area/index.html ","admin/controlpanel.php ","admincp/index.asp ","admincp/login.asp ","admincp/index.html ","admin/account.html ","adminpanel.html ","webadmin.html ","webadmin/index.html ","webadmin/admin.html ","webadmin/login.html ","admin/admin_login.html ","admin_login.html ","panel-administracion/login.html","admin/cp.php ","cp.php ","administrator/index.php ","administrator/login.php ","nsw/admin/login.php ","webadmin/login.php ","admin/admin_login.php ","admin_login.php ","administrator/account.php ","administrator.php ","admin_area/admin.html","pages/admin/admin-login.php","admin/admin-login.php ","admin-login.php ","bb-admin/index.html ","bb-admin/login.html ","bb-admin/admin.html ","admin/home.html ","modelsearch/login.php ","moderator.php ","moderator/login.php ","moderator/admin.php ","account.php ","pages/admin/admin-login.html ","admin/admin-login.html ","admin-login.html ","controlpanel.php ","admincontrol.php ","admin/adminLogin.html","adminLogin.html","admin/adminLogin.html ","home.html ","rcjakar/admin/login.php ","adminarea/index.html ","adminarea/admin.html ","webadmin.php ","webadmin/index.php ","webadmin/admin.php ","admin/controlpanel.html ","admin.html ","admin/cp.html ","cp.html ","adminpanel.php ","moderator.htm","administrator/index.html","administrator/login.html ","user.html ","administrator/account.html ","administrator.html ","login.html ","modelsearch/login.html ","moderator/login.html ","adminarea/login.html ","panel-administracion/index.html ","panel-administracion/admin.html ","modelsearch/index.html ","modelsearch/admin.html ","admincontrol/login.html ","adm/index.html ","adm.html ","moderator/admin.html ","user.php ","account.html ","controlpanel.html ","admincontrol.html ","panel-administracion/login.php ","wp-login.php ","adminLogin.php ","admin/adminLogin.php ","home.php ","adminarea/index.php ","adminarea/admin.php ","adminarea/login.php ","panel-administracion/index.php ","panel-administracion/admin.php ","modelsearch/index.php ","modelsearch/admin.php ","admincontrol/login.php ","adm/admloginuser.php ","admloginuser.php ","admin2.php ","admin2/login.php ","admin2/index.php ","adm/index.php ","adm.php ","affiliate.php ","adm_auth.php ","admin ","admin.asp ","admin.aspx ","admin.cfm ","admin.html ","admin.php ","admin.xhtml ","admin/ ","wp-admin ","wp-admin/ ","wp-login.php ","wp-login/ ","admin/account.asp ","admin/account.cfm ","admin/account.html ","admin/account.php ","admin/admin.asp ","admin/admin.cfm ","admin/admin.html ","admin/admin.php ","admin/admin_login.asp ","admin/admin_login.cfm ","admin/admin_login.html ","admin/admin_login.php ","admin/admin-login.asp ","admin/adminLogin.asp ","admin/admin-login.cfm ","admin/adminLogin.cfm ","admin/admin-login.html ","admin/adminLogin.html ","admin/admin-login.php ","admin/adminLogin.php ","admin/controlpanel.asp ","admin/controlpanel.cfm ","admin/controlpanel.html ","admin/controlpanel.php ","admin/cp.asp ","admin/cp.cfm ","admin/cp.html ","admin/cp.php ","admin/home.asp ","admin/home.cfm ","admin/home.html ","admin/home.php ","admin/index.asp ","admin/index.cfm ","admin/index.html ","admin/index.php ","admin/login.asp ","admin/login.cfm ","admin/login.html ","admin/login.php ","account.asp ","account.cfm ","account.html ","account.php ","acct_login/ ","adm ","adm.asp ","adm.cfm ","adm.html ","adm.php ","adm/ ","adm/admloginuser.asp ","adm/admloginuser.cfm ","adm/admloginuser.php ","adm/index.asp ","adm/index.cfm ","adm/index.html ","adm/index.php ","adm_auth.asp ","adm_auth.cfm ","adm_auth.php ","admin_area ","admin_area/ ","admin_area/admin.asp ","admin_area/admin.cfm ","admin_area/admin.html ","admin_area/admin.php","admin_area/index.asp ","admin_area/index.cfm","admin_area/index.html ","admin_area/index.php ","admin_area/login.asp ","admin_area/login.cfm ","admin_area/login.html ","admin_area/login.php ","admin_login.asp ","admin_login.cfm ","admin_login.html ","admin_login.php ","admin1.asp ","admin1.html ","admin1.php ","admin1/ ","admin2.asp ","admin2.cfm ","admin2.html ","admin2.php ","admin2/index.asp ","admin2/index.cfm ","admin2/index.php ","admin2/login.asp ","admin2/login.cfm ","admin2/login.php ","admin4_account/ ","admin4_colon/ ","adminarea ","adminarea/admin.asp ","adminarea/admin.cfm ","adminarea/admin.html ","adminarea/admin.php ","adminarea/index.asp ","adminarea/index.cfm","adminarea/index.html ","adminarea/index.php ","adminarea/login.asp ","adminarea/login.cfm ","adminarea/login.html ","adminarea/login.php ","admincontrol.asp ","admincontrol.cfm ","admincontrol.html ","admincontrol.php ","admincontrol/login.asp ","admincontrol/login.cfm ","admincontrol/login.html ","admincontrol/login.php ","admincp/index.asp ","admincp/index.cfm ","admincp/index.html ","admincp/login.asp ","admincp/login.cfm ","administer/ ","administr8.asp ","administr8.html ","administr8.php","administr8/ ","administratie/ ","administration.html ","administration.php ","administration/ ","administrator","administrator.asp","administrator.cfm ","administrator.html ","administrator.php ","administrator/ ","administrator/account.asp ","administrator/account.cfm ","administrator/account.html ","administrator/account.php ","administrator/index.asp ","administrator/index.cfm ","administrator/index.html ","administrator/index.php ","administrator/login.asp ","administrator/login.cfm ","administrator/login.html ","administrator/login.php ","administratoraccounts/ ","administratorlogin ","administratorlogin.asp ","administratorlogin.cfm ","administratorlogin.php ","administrators/","administrivia/ ","adminLogin ","admin-login.asp ","adminLogin.asp ","admin-login.cfm ","adminLogin.cfm ","admin-login.html ","adminLogin.html ","admin-login.php ","adminLogin.php ","adminpanel.asp ","adminpanel.cfm ","adminpanel.html ","adminpanel.php","adminpro/ ","admins.asp ","admins.html ","admins.php ","admins/ ","AdminTools/ ","admloginuser.asp ","admloginuser.cfm ","admloginuser.php ","affiliate.asp ","affiliate.cfm ","affiliate.php ","autologin/ ","banneradmin/ ","bb-admin ","bbadmin/ ","bb-admin/admin.asp ","bb-admin/admin.cfm ","bb-admin/admin.html ","bb-admin/admin.php ","bb-admin/index.asp ","bb-admin/index.cfm ","bb-admin/index.html ","bb-admin/index.php ","bb-admin/login.asp ","bb-admin/login.cfm ","bb-admin/login.html ","bb-admin/login.php ","bigadmin/ ","blogindex/ ","cadmins/ ","ccp14admin/ ","Clave/ ","cmsadmin/","controlpanel.asp","controlpanel.cfm","controlpanel.html","controlpanel.php","controlpanel/","cp.asp","cp.cfm ","cp.html","cp.php","cpanel/","cPanel/","cpanel_file/ ","customer_login/ ","database_administration/ ","Database_Administration/ ","directadmin/ ","dir-login/ ","ezsqliteadmin/ ","fileadmin.asp ","fileadmin.html ","fileadmin.php ","fileadmin/ ","formslogin/ ","globes_admin/ ","home.asp ","home.cfm ","home.html ","home.php ","hpwebjetadmin/ ","Indy_admin/ ","instadmin ","irc-macadmin/ ","LiveUser_Admin/ ","login.asp ","login.cfm ","login.html ","login.php ","login_db/ ","login1/ ","loginflat/ ","login-redirect/ ","login-us/ ","logo_sysadmin/ ","Lotus_Domino_Admin/ ","macadmin/ ","manage ","manuallogin/ ","memberadmin ","memberadmin.asp ","memberadmin.cfm ","memberadmin.php ","members/ ","memlogin/ ","meta_login/ ","modelsearch/admin.asp ","modelsearch/admin.cfm ","modelsearch/admin.html","modelsearch/admin.php ","modelsearch/index.asp ","modelsearch/index.cfm","modelsearchindex.html","modelsearch/index.php ","modelsearch/login.asp ","modelsearch/login.cfm ","modelsearch/login.html","modelsearchlogin.php","moderator","moderator.asp","moderator.cfm ","moderator.html ","moderator.php ","moderator/ ","moderator/admin.asp ","moderator/admin.cfm ","moderator/admin.html ","moderator/admin.php ","moderator/login.asp ","moderator/login.cfm ","moderator/login.html ","moderator/login.php ","myadmin/ ","navSiteAdmin/ ","newsadmin/ ","nsw/admin/login.php ","openvpnadmin/ ","P/W/ ","pages/admin/admin-login.asp","pages/admin/admin-login.cfm","pages/admin/admin-login.html ","pages/admin/admin-login.php ","panel/ ","panel-administracion ","panel-administracion/admin.asp ","panel-administracion/admin.cfm ","panel-administracion/admin.html ","panel-administracion/admin.php ","paneladministracion/index.asp ","panel-administracion/index.cfm ","panel-administracion/index.html","panel-administracion/index.php ","panel-administracion/login.asp ","panel-administracion/login.cfm ","panel-administracion/login.html ","panel-administracion/login.php ","passe/ ","password/ ","Password/ ","PASSWORD/ ","Personal/ ","pgadmin/","phpldapadmin/ ","phpmyadmin/ ","phppgadmin/ ","phpSQLiteAdmin/ ","platz_login/ ","power_user/ ","project-admins/","pureadmin/ ","radmind/","radmind-1/ ","rcjakar/admin/login.php ","rcLogin/ ","senha/ ","Senha/ ","Server.asp ","Server.html","Server.php ","server/ ","Server/ ","server_admin_small/ServerAdministrator/ ","showlogin/ ","simpleLogin/ ","Sing/ ","siteadmin/index.asp ","siteadmin/index.cfm ","siteadmin/index.php ","siteadmin/login.asp ","siteadmin/login.cfm ","siteadmin/login.html","siteadmin/login.php","smblogin/","sql-admin/","ss_vms_admin_sm/","sshadmin/","staradmin/ ","sub-login/ ","Super-Admin/ ","support_login/ ","sysadmin.asp ","sysadmin.html ","sysadmin.php ","sysadmin/","sysadmin/","SysAdmin/ ","SysAdmin2/ ","sysadmins/ ","system_administration/ ","system-administration/ ","typo3/ ","ur-admin.asp ","ur-admin.html","ur-admin.php ","ur-admin/ ","usager/ ","Usager/ ","user.asp ","user.cfm ","user.html ","user.php ","useradmin/","UserLogin/","username/","Username/","USERNAME/ ","Usuario/ ","utility_login/ ","vadmind/","vmailadmin/","webadmin","webadmin.asp","webadmin.cfm ","webadmin.html ","webadmin.php ","webadmin/","WebAdmin/","webadmin/admin.asp ","webadmin/admin.cfm ","webadmin/admin.html ","webadmin/admin.php","webadmin/index.asp ","webadmin/index.cfm ","webadmin/index.html ","webadmin/index.php ","webadmin/login.asp ","webadmin/login.cfm ","webadmin/login.html ","webadmin/login.php ","wizmysqladmin/ ","wp-admin","wp-admin/","wp-login.php ","wp-login/ ","xlogin/ ","yonetici.asp ","yonetici.html ","yonetici.php","yonetim.asp","yonetim.html","yonetim.php","ser.asp ","panel.asp ","admin/login.htm","administratorlogin.php ","cp.asp ","admin.php","administrators.php","relogin.htm","log-in.asp","controlpanel.asp ","controlpanel/ ","vadmind/ ","log-in.php ","authadmin.php ","xlogin/ ","server_admin_small/","admincp/login.php ","adm_auth.asp ","checkadmin.asp ","adminpro/ ","loginflat/ ","bb-admin/login.asp","news_detail.php","Indy_admin/","adminitem.asp","vorod.php","moderator/login.asp ","login1/ ","irc-macadmin/","superuser.php","pureadmin/","formslogin/","adminitems/","sysadm/","0manager/","Server/","phpldapadmin/ ","myadmin/ ","yonetim.html","adminLogin/vorod/","sysadm.asp","loginok/","root/","yonetim.php","loginphp","index.swf","loginsave/","admin1.htm ","dir-login/ ","wp-login.php ","superuserasp","moderator/admin.asp','adminsite/ ","logoutasp ","access/","cpanel_file/","sysadmins/","moderator.php","relogin.php","users/","smblogin/","navSiteAdmin/","isadmin.php ","sign-in.php","memlogin/","phppgadmin/ ","management.asp ","/panel/about_edit.php ","instadmin/ ","bb-admin/admin.html ","0admin/ ","affiliate.php ","meta_login/ ","signin.php ","superuser.asp","loginsuper/ ","vorod.asp ","aadmin/","ur-admin.php ","yonetici.asp ","admin/controlpanel.asp ","administr8.asp","signin.asp","administration/","admin2.asp ","blogindex/","ur-admin/","admincontrol.php","cgi-bin/loginasp ","cgi-bin/loginphp ","adm.php","admin_login.asp","administration.php","login-us/","supermanagerasp","moderator/admin.php ","admin/account.php","Server.asp","useradmin/","adminlogin.php","bigadmin/","moderator.asp ","login_adminasp","authentication.asp","power_user/","modules/admin/","admin1.asp ","platz_login/","manager/ ","logout/","manage/","adminadmin.asp","moderator/login.php","pages/admin/admin-login.php ","fileadmin.asp ","wp-admin/ ","logo_sysadmin/ ","admin/adminLogin.htm","bb-admin/admin.asp","pages/admin/","processlogin.php","loginsuperphp","super1php","uvpanel/","macadmin/","system_administration/ ","admin/cp.php","admin4_account/","sysadmin.php","control.php","supermanphp","super_indexasp","admin/adminLogin.php","panel-administracionlogin.php","admin/account.html","admins.php","log_in.php","admins.asp","radmind-1/","sysadm.php","staradmin/","login_db/","userlogin.php","secrets/","accounts.php","security/","security-admin.php","security-login.php","security/admin.php","security/login.php","login/","security/user","manage.php"}





print (' work begin ' + site + ' ...\n\n')

print





try:

    for admin in pg:

        admin = admin.replace('\n\n','')

        admin = '/' + admin

        mtucxdz = httplib.HTTPConnection(site)

        mtucxdz.request('GET',admin)

        mtucxdz = mtucxdz.getresponse()

        print '%s %s %s' % (admin, mtucxdz.status, mtucxdz.reason)

        if mtucxdz.status == 200:

                        raw_input(g+"[*] Loginnya disini bosQ, Lanjut? tekan ENTER .\n" +w)



except (KeyboardInterrupt, SystemExit):

    print w+'  '
