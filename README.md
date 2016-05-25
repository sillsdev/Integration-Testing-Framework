# Integration-Testing-Framework
Project to store files related to automating testing for SIL Software on Linux and Windows

Contributors
* SIL LS Dev Team
* Ryan McCoppin
* Jessica Dawson
* Karl Rogers

Packaging a Vagrant Box: 
C:\Users\mccoppinR>vagrant package --base box_to_package --output ubuntu64

Run Script as root: sudo -u root command

*BIG PICTURE*
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
