# Base
FROM golang:1.20.4-alpine

WORKDIR /app/conduit-replay
RUN apk add build-base make gcc g++ linux-headers git libpcap libpcap-dev
RUN apk update && apk upgrade && apk add --no-cache ca-certificates
RUN update-ca-certificates

RUN wget https://github.com/vc-pvp/conduit-replay/archive/refs/tags/v2.0.0-rc1.tar.gz -O replay.tar.gz
RUN tar xzf replay.tar.gz
COPY /app/conduit-replay/conduit-replay-2.0.0-rc1 /go/src

WORKDIR /go/src
RUN go mod vendor
RUN go build -mod=vendor -o conduit-replay -tags netgo

COPY /go/src/conduit-replay /go/bin
RUN chmod +x /go/bin/conduit-replay

WORKDIR /go/bin
ENTRYPOINT ["./conduit-replay"]
