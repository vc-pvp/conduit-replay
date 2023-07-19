# Base
FROM docker-hub.repo.viacom.com/golang:1.20.4-alpine as base

WORKDIR /app/src
RUN apk add build-base make gcc g++ linux-headers git libpcap libpcap-dev
RUN apk update && apk upgrade && apk add --no-cache ca-certificates
RUN update-ca-certificates

COPY go.mod go.sum ./
COPY *.go ./
COPY cmd ./cmd
COPY proto ./proto
COPY internal ./internal
COPY middleware ./middleware

FROM base as builder

WORKDIR /app/build/
COPY --from=base /app/src/ .
RUN go mod vendor
RUN GOOS=linux GOARCH=arm64 go build -mod=vendor -o conduit-replay -tags netgo -ldflags "-extldflags \"-static\""

FROM scratch
WORKDIR /app/replay/bin
COPY --from=base /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
COPY --from=builder /app/replay/src/conduit-replay .
ENTRYPOINT ["./conduit-replay"]
