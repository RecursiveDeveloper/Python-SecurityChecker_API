resource "aws_instance" "sample_Ec2_instance" {
    ami = "ami-0b5eea76982371e91"
    instance_type = "t2.micro"

    user_data = <<-EOF
        #!/bin/bash
        sudo yum update -y
        sudo yum -y install httpd -y
        sudo service httpd start
        echo "Hello world from EC2 $(hostname -f)" > /var/www/html/index.html
		EOF

    vpc_security_group_ids = [ aws_security_group.sg_instance.id ]

    tags = {
        Name = "SampleEC2Instance"
        Environment = "Development"
        Owner = "RecursiveDeveloper"
    }
}

resource "aws_security_group" "sg_instance" {
    name = "tf_tcp_security_group"

    ingress {
      from_port = 80
      to_port = 80
      protocol = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
    }

    egress {
      from_port = 0
      to_port = 0
      protocol = "-1"
      cidr_blocks = ["0.0.0.0/0"]
    }
}
