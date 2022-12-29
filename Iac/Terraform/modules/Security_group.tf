resource "aws_security_group" "sg_instance" {
    name = "tf_tcp_security_group"

    ingress = {
      from_port = 80
      to_port = 80
      protocol = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
    } 

    egress = {
      from_port = 80
      to_port = 80
      protocol = "-1"
      cidr_blocks = ["0.0.0.0/0"]
    }
}
