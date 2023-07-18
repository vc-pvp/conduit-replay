# Base
FROM --platform=linux/arm64 golang:1.20.4-alpine as base

WORKDIR /app/conduit-replay
RUN apk add build-base make gcc g++ linux-headers git libpcap libpcap-dev
RUN apk update && apk upgrade && apk add --no-cache ca-certificates
RUN update-ca-certificates

RUN wget https://github.com/vc-pvp/conduit-replay/archive/refs/tags/v2.0.0-rc1.tar.gz -O replay.tar.gz
RUN tar xzf replay.tar.gz

# Build stage
FROM base as builder

WORKDIR /app/replay
COPY --from=base /app/conduit-replay/conduit-replay-2.0.0-rc1 /app/replay
RUN go mod vendor
RUN go build -mod=vendor -o conduit-replay -tags netgo -ldflags "-extldflags \"-static\""

# Output
FROM scratch
COPY --from=base /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
COPY --from=builder /app/replay/conduit-replay .
ENTRYPOINT ["./conduit-replay"]
