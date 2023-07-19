# Base
FROM --platform=linux/arm64 golang:1.20.4-alpine as base

WORKDIR /app/replay
RUN apk add build-base make gcc g++ linux-headers git libpcap libpcap-dev
RUN apk update && apk upgrade && apk add --no-cache ca-certificates
RUN update-ca-certificates

RUN wget https://github.com/vc-pvp/conduit-replay/archive/refs/tags/v2.0.0-rc1.tar.gz -O replay.tar.gz
RUN tar xzf replay.tar.gz
COPY /app/replay/conduit-replay-2.0.0-rc1 /go/src

FROM base as builder
WORKDIR /go/src
RUN go mod vendor
RUN go build -mod=vendor -o conduit-replay -tags netgo
COPY /go/src/conduit-replay /go/bin
RUN chmod +x /go/bin/conduit-replay

FROM scratch
WORKDIR /go/bin
COPY --from=base /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
ENTRYPOINT ["./conduit-replay"]
