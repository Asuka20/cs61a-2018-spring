; Q1
(define (compose-all funcs)
  (if (null? funcs) 
      (lambda (x) x)
      (lambda (x) ((compose-all (cdr funcs)) ((car funcs) x)))))

; Q2
(define (tail-replicate x n)
  (define (helper res k) 
    (if (= k 0)
        res
        (helper (cons x res) (- k 1))))
  (helper () n))