# linux_setup
Project to store files related to automating testing for SIL Software on Linux

vagrant up, vagrant ssh, vagrant halt, vagrant destroy

vagrant provision, vagrant ssh-config

Packaging a Vagrant Box
C:\Users\mccoppinR>vagrant package --base box_to_package
--output ubuntu64

Run Script as root
sudo -u root command

Set permissions
find . -name '.*' -prune -o -exec chmod u=rwx,g=rx,o=r {} +
chown -R vagrant folder/

*REPORT EVERY ERROR*
If expect breaks, needs to be reported


Need to do:
^Check that we can auto install fieldworks

^Get common share file working…

Have linux scripts write and read data to shared directory

Startup Scripts

sleep 6m && sikuli_runall.sh

sleep 5m && fieldworks-flex


Generica

^Install VirtualBox

^Install Git  =  put git commands on windows shell

^Install Vagrant

^Use Vagrant File (Ryan’s) OR follow tutorial at Vagrant website. Boot into a linux machine!

^Use “expect” script to install FLEX

Auto open FLEX and run script sikuli_runall.sh

