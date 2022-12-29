resource "aws_instance" "sample_Ec2_instance" {
    ami = "ami-0b5eea76982371e91"
    instance_type = "t2.micro"

    tags = {
        Name = "SampleEC2Instance"
        Environment = "Development"
        Owner = "RecursiveDeveloper"
    }
}
