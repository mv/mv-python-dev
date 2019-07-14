# -*- mode: ruby -*-
# vi: set ft=ruby :


Vagrant.configure("2") do |config|

  config.vm.box = "gbailey/amzn2"

  # config.vm.provider "virtualbox" do |vb|
  #   # Display the VirtualBox GUI when booting the machine
  #   vb.gui = true
  #
  #   # Customize the amount of memory on the VM:
  #   vb.memory = "1024"
  # end

  config.vm.network "private_network", ip: "192.168.33.11"

  config.vm.provision "shell", inline: <<-SHELL
    yum install -y yum-utils git
    yum install -y htop dstat lsof
    yum install -y python3 python3-pip python3-devel
  SHELL

  config.vm.provision "shell", path: "util/provision.pyenv.linux.sh"

end

