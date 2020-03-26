package main

import (
	"encoding/json"
	"math/rand"
	"net/http"
	"sync"
	"strconv"
	"io/ioutil"

	"github.com/julienschmidt/httprouter"
	"github.com/beorn7/perks/quantile"
	"github.com/satori/go.uuid"
)

func main() {
	s := newServer()
	router := httprouter.New()
	router.POST("/", s.Create)
	router.GET("/:id", s.Read)
	router.POST("/:id/samples", s.Insert)
	router.PUT("/:id", s.Reset)
	router.DELETE("/:id", s.Remove)
	log.Fatal(http.ListenAndServe(":8080", router))
}

type stream struct {
	ID string `json:"id"`
	Limits []float64 `json:"limits"`
	Targets map[float64]float64 `json:"targets"`
	Values []float64 `json:"values"`
	Samples []float64 `json:"samples"`
	Quantiles map[float64]float64 `json:"quantiles"`
	str *quantile.Stream
}

type server struct {
	streams map[string]*stream
	mu *sync.Mutex
}

func newServer() server {
	return &server{
		streams: make(map[string]stream),
		mu: &sync.Mutex{},
	}
}

func (s server) Create(w http.ResponseWriter, r *http.Request, p httprouter.Params) {
	st := &stream{}
	if err := json.Unmarshal(st); err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}
	st.ID = uuid.NewV4().String()
	st.str = quantile.NewTargeted(st.Targets)
	s.mu.Lock()
	s.streams[s.ID] = st
	s.mu.Unlock()
	w.WriteHeader(http.StatusOK)
}

func (s server) Read(w http.ResponseWriter, r *http.Request, p httprouter.Params) {
	s.mu.Lock()
	st, ok := s.streams[p.ByName("id")]
	s.mu.Unlock()
	if !ok {
		w.WriteHeader(http.StatusNotFound)
		return
	}
	buf, err := json.Marshal(st)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	w.WriteHeader(http.StatusOk)
	_, _ = w.Write(buf)
}

func (s server) Insert(w http.ResponseWriter, r *http.Request, p httprouter.Params) {
	payload, err := ioutil.ReadAll(r.Body)
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}
	value, err := strconv.ParseFloat(payload)
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}
	id := p.ByName("id")
	s.mu.Lock()
	if st, ok := s.streams[id]; ok {
		st.Values = append(st.Values, value)
		st.str.Insert(value)
	}
	s.mu.Unlock()
	if !ok {
		http.Error(w, "stream not found", http.StatusNotFound)
		return
	}
	w.WriteHeader(http.StatusOK)
}

func (s server) Reset(w http.ResponseWriter, r *http.Request, p httprouter.Params) {
}

func (s server) Remove(w http.ResponseWriter, r *http.Request, p httprouter.Params) {
}



/*
func main() {
	high := quantile.NewHighBiased(0.1)
	low := quantile.NewLowBiased(0.0)
	targeted := quantile.NewTargeted(map[float64]float64{
		0.99: 0.01, 0.90: 0.05, 0.50: 0.1,
	})
	items := make([]float64, 50)

	for i := 0; i < 50; i++ {
		item := float64(rand.Intn(100))
		items[i] = item
		high.Insert(item)
		low.Insert(item)
		targeted.Insert(item)
	}
	fmt.Printf(">>>>>> items: %+v\n", items)
	fmt.Println("High:")
	fmt.Println("====== 90% :", high.Query(0.9))
	fmt.Printf(">>>>>> samples: %+v\n", high.Samples())
	fmt.Println("Low:")
	fmt.Println("====== 10% : ", high.Query(0.1))
	fmt.Printf(">>>>>> low: %+v\n", low.Samples())
	fmt.Println("Targeted:")
	fmt.Println("====== 99% :", targeted.Query(0.99))
	fmt.Println("====== 90% :", targeted.Query(0.99))
	fmt.Println("====== 50% :", targeted.Query(0.50))
	fmt.Printf(">>>>>> targeted: %+v\n", targeted.Samples())

	//data, err := json.Marshal(items)
	//if err != nil { panic(err) }
	//fmt.Printf("items: %s\n", data)

	//data, err = json.Marshal(high.Samples())
	//if err != nil { panic(err) }
	//fmt.Printf("items: %s\n", data)
	//data, err = json.Marshal(accumulate(high.Samples()))
	//if err != nil { panic(err) }
	//fmt.Printf("items: %s\n", data)

	//fmt.Println("low:", low.Samples())

	//fmt.Printf(">>>>>>%+v\n", targeted.Samples())
	//data, err = json.Marshal(accumulate(targeted.Samples()))
	//if err != nil { panic(err) }
	//fmt.Printf(">>>>>>%s\n", data)
	//fmt.Println("targeted:", data)
}

type Sample struct {
	Value float64 `json:"value"`
	Low float64 `json:"low"`
	High float64 `json:"high"`
}

func accumulate(samples quantile.Samples) []Sample {
	out := make([]Sample, len(samples))
	var low float64 = 0
	var high float64 = 0
	for i, s := range samples {
		low += s.Width
		high = low + s.Delta
		out[i] = Sample{
			Value: s.Value,
			Low: low,
			High: high,
		}
	}
	return out
}
*/
