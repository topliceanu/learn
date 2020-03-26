package main

import (
	"fmt"
	"math"
	// "math/rand"

	"github.com/prometheus/client_golang/prometheus"
	dto "github.com/prometheus/client_model/go"
	"github.com/golang/protobuf/proto"
)

func main() {
	temps := prometheus.NewSummary(prometheus.SummaryOpts{
		Name:       "pond_temperature_celsius",
		Help:       "The temperature of the frog pond.",
		Objectives: map[float64]float64{0.5: 0.1, 0.9: 0.05, 0.99: 0.01},
	})

	// Simulate some observations.
	for i := 0; i < 100; i++ {
		//temps.Observe(float64(rand.Intn(100)))
		temps.Observe(30 + math.Floor(120*math.Sin(float64(i)*0.1))/10)
	}

	// Just for demonstration, let's check the state of the summary by
	// (ab)using its Write method (which is usually only used by Prometheus
	// internally).
	metric := &dto.Metric{}
	temps.Write(metric)
	fmt.Println(proto.MarshalTextString(metric))
}
