# Integration-Testing-Framework
Project to store files related to automating testing for SIL Software on Linux

Packaging a Vagrant Box: 
C:\Users\mccoppinR>vagrant package --base box_to_package
--output ubuntu64

Run Script as root: sudo -u root command

Set permissions
* find . -name '.*' -prune -o -exec chmod u=rwx,g=rx,o=r {} +
* chown -R vagrant folder/

*REPORT EVERY ERROR*
* If expect breaks, needs to be reported


Need to do:

Generica

  * Install VirtualBox

  * Install Git  =  put git commands on windows shell

  * Install Vagrant

  * Use Vagrant File (Ryan’s) OR follow tutorial at Vagrant website. Boot into a linux machine!

  * Auto open FLEX and run script sikuli_runall.sh by Vagrantfile

