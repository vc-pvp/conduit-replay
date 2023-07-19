# Base
FROM docker-hub.repo.viacom.com/golang:1.20.4-alpine as base

WORKDIR /app/replay
RUN apk add build-base make gcc g++ linux-headers git libpcap libpcap-dev
RUN apk update && apk upgrade && apk add --no-cache ca-certificates
RUN update-ca-certificates

COPY go.mod ./src
COPY *.go ./src
COPY cmd ./src/cmd/
COPY internal ./src/internal/
COPY middleware ./src/middleware/

FROM base as builder

WORKDIR /app/replay/src
RUN go mod vendor
RUN GOOS=linux GOARCH=arm64 go build -mod=vendor -o conduit-replay -tags netgo -ldflags "-extldflags \"-static\""

FROM scratch
WORKDIR /app/replay/bin
COPY --from=base /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
COPY --from=builder /app/replay/src/conduit-replay .
ENTRYPOINT ["./conduit-replay"]
