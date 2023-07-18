group "default" {
  targets = ["conduit-replay"]
}

target "conduit-replay" {
  dockerfile = "./deploy/Dockerfile"
  platforms = ["linux/arm64"]
}
