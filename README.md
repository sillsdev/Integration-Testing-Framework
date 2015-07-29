# Integration-Testing-Framework
Project to store files related to automating testing for SIL Software on Linux

Packaging a Vagrant Box: 
C:\Users\mccoppinR>vagrant package --base box_to_package
--output ubuntu64

Run Script as root: sudo -u root command

*BIG PICTURE*
* Powershell 
  * presents options for os (linux, windows, etc), software suite (FLEx, Bloom, etc)
    * uses software suite to load test scripts from proper repo
    * uses software suite to edit Vagrant file (perl script?)
      * for right suite link
      * for right test scripts link (from repo)
    * interface allows user to choose scripts to use
      * scripts written to file
      * later read by bash
 * calls vagrant up followed by vagrant reload

* Vagrant
 * Installs software and scripts
 * Boots software and scripts in "auto run" folder
 * Reboot login starts scripts

* Bash/Shell
  * Select "use scripts"
  * Startup chosen software
  * Python/Sikuli
    * Sikuli control scripts
    * Report errors

*REPORT EVERY ERROR*
* If expect breaks, needs to be reported

Generica
  * Install VirtualBox
  * Install Git  =  put git commands on windows shell
  * Install Vagrant
  * Use VagrantFile  OR follow tutorial at Vagrant website. Boot into a linux machine!
    * Use vagrant/installauto to create base machine
    * Package base machine
    * Use vagrant/flexauto (or other) to install flex and tests for auto testing
      * Auto-opens FLEX and runs script sikuli_runall.sh (or other)

Helpful documentation
https://docs.google.com/document/d/1wCPwGvsdLk8Luqwc88LKxAuzzPnOuiFySG3Uw9fPhPc/edit?usp=sharing
