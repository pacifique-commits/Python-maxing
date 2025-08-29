Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/focal64"
  
  # Forward SSH for easy access
  config.ssh.insert_key = false

  # Provision Python
  config.vm.provision "shell", inline: <<-SHELL
    apt-get update -y
    apt-get install -y python3 python3-pip
  SHELL
end

