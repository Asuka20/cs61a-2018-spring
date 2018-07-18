(define (accumulate combiner start n term)
  (if (= n 0)
      start
      (combiner (term n) (accumulate combiner start (- n 1) term))
  )
)

(define (accumulate-tail combiner start n term)
  (define (helper n result)
   (if (= n 0)
    result
    (helper (- n 1) (combiner (term n) result))))
  (helper n start))

(define-macro (list-of expr for var in seq if filter-fn)
  `(map (lambda (,var) ,expr) (filter (lambda (,var) ,filter-fn) ,seq)))
    
