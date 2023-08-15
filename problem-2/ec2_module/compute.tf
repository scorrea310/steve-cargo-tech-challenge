resource "aws_instance" "my_ec2" {
  ami           = var.ami
  instance_type = var.instance_type
  user_data     = <<-EOF
              #!/bin/bash
              sudo yum update -y 
              sudo yum install -y python3 
              python3 --version
              EOF
}

# Note: The Amazon Linux 2023 ec2 already has python 3.9 so running
# 'sudo yum install -y python3' doesn't actually do anything. I think
# its because 3.9 is the latest available version in the amazon linux 2023 repo. 
# However, you can install the latest python3 version (3.11). You 
# would need to run 'sudo yum install python3.11.x86_64'. There are other methods like pyenv.
