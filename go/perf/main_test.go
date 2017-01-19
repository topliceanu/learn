package main

import (
	"net/http"
	"net/http/httptest"
	"testing"
	"strings"
)

func TestHandler(t *testing.T) {
	cases := []struct{
		in, out string
	}{
		{"campoy@golang.org", "gopher campoy"},
		{"something", "dear something"},
	}
	for _, c := range cases {
		req, err := http.NewRequest(http.MethodGet, "http://localhost:8080/"+c.in, nil)
		if err != nil {
			t.Fatalf("Could not create request: %v", err)
		}
		rec := httptest.NewRecorder()
		handler(rec, req)
		if rec.Code != http.StatusOK {
			t.Fatalf("Expected status 200 ok; got %d", rec.Code)
		}
		if !strings.Contains(rec.Body.String(), c.out) {
			t.Fatalf("Expected %s in response body but got: %q", c.out, rec.Body.String())
		}
	}
}
