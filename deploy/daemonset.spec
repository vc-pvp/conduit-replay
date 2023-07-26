kind: DaemonSet
apiVersion: apps/v1
metadata:
  name: conduit-replay
  namespace: pvp
spec:
  selector:
    matchLabels:
      name: conduit-replay
  template:
    metadata:
      labels:
        name: conduit-replay
    spec:
      containers:
        - name: conduit-replay
          image: vdock.repo.viacom.com/cge/viacbs/github.com/vc-pvp/conduit-replay/conduit-replay/conduit-replay:57
          args:
            - '--input-raw'
            - <K8_DEPLOYMENT>#<k8s://pvp/deployment/conduit-server-dev-conduit
            - '--input-raw-track-response'
            - '--input-raw-ignore-interface'
            - ens5
            - '--input-raw-ignore-interface'
            - cilium_geneve
            - '--input-raw-ignore-interface'
            - cilium_host
            - '--input-raw-ignore-interface'
            - cilium_net
            - '--output-kafka-host'
            - <KAFKA_HOST>
            - '--output-kafka-topic'
            - <KAFKA_TOPIC>
            - '--output-kafka-use-sasl'
            - '--output-kafka-mechanism'
            - <KAFKA_MECHANISM>
            - '--output-kafka-username'
            - <KAFKA_USER>>
            - '--output-kafka-password'
            - <KAFKA_PASSWORD>
            - '--output-kafka-json-format'
            - '--http-disallow-header'
            - 'User-Agent: ELB-HealthChecker/2.0'
            - '--http-disallow-header'
            - 'User-Agent: kube-probe/1.25'
            - '--http-disallow-header'
            - 'User-Agent: Prometheus/2.39.1'
          resources:
            limits:
              cpu: 1
              memory: 2
            requests:
              cpu: 1
              memory: 2
          imagePullPolicy: IfNotPresent
      restartPolicy: Always
      terminationGracePeriodSeconds: 30
      nodeSelector:
        k8s.viacbs.tech/nodepool: pvp-arm64
      serviceAccount: conduit-orchestrator-dev-conduit-orc-vmn-read-only
      hostNetwork: true
      imagePullSecrets:
        - name: cge-pull
      tolerations:
        - key: k8s.viacbs.tech/pvp-arm64
          operator: Exists
          effect: NoSchedule
        - key: k8s.viacbs.tech/pvp-arm64
          operator: Exists
          effect: NoExecute
