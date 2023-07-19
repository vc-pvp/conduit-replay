# Base
FROM --platform=linux/arm64 golang:1.20.4-alpine as base

WORKDIR /app/replay
RUN apk add build-base make gcc g++ linux-headers git libpcap libpcap-dev
RUN apk update && apk upgrade && apk add --no-cache ca-certificates
RUN update-ca-certificates

RUN wget https://github.com/vc-pvp/conduit-replay/archive/refs/tags/v2.0.0-rc1.tar.gz -O replay.tar.gz
RUN tar xzf replay.tar.gz

FROM base as builder
WORKDIR /app/replay/src
COPY --from=base /app/replay/conduit-replay-2.0.0-rc1 .

RUN go mod vendor
RUN go build -mod=vendor -o conduit-replay -tags netgo

COPY ./conduit-replay /app/replay/bin
RUN chmod +x /app/replay/bin/conduit-replay

FROM scratch
WORKDIR /app/replay/bin
COPY --from=base /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
ENTRYPOINT ["./conduit-replay"]
