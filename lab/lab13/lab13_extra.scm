; Q4
(define (rle s)
  (define (helper node prev count) 
    (cond ((null? node) (cons-stream (list prev count) nil))
          ((= prev (car node)) (helper (cdr-stream node) prev (+ count 1)))
          (else (cons-stream (list prev count) (helper (cdr-stream node) (car node) 1)))))
  (if (null? s)
      ()
      (helper (cdr-stream s) (car s) 1)))

; Q4 testing functions
(define (list-to-stream lst)
    (if (null? lst) nil
                    (cons-stream (car lst) (list-to-stream (cdr lst))))
)

(define (stream-to-list s)
    (if (null? s) nil
                 (cons (car s) (stream-to-list (cdr-stream s))))
)

; Q5
(define (insert n s)
  (define (helper prevs node)
    (cond ((null? node) (append prevs (list n)))
        ((> (car node) n) (append (append prevs (list n)) node))
        (else (helper (append prevs (list (car node))) (cdr node)))))
  (helper () s))

; Q6
(define (deep-map fn s)
  (cond ((null? s) nil)
        ((list? (car s)) (cons (deep-map fn (car s)) (deep-map fn (cdr s))))
        (else (cons (fn (car s)) (deep-map fn (cdr s))))))


; Q7
; Feel free to use these helper procedures in your solution
(define (map fn s)
  (if (null? s) nil
      (cons (fn (car s))
            (map fn (cdr s)))))

(define (filter fn s)
  (cond ((null? s) nil)
        ((fn (car s)) (cons (car s)
                            (filter fn (cdr s))))
        (else (filter fn (cdr s)))))

; Implementing and using these helper procedures is optional. You are allowed
; to delete them.
(define (count name s)
  (cond ((null? s) 0)
        ((eq? (car s) name) (+ 1 (count name (cdr s))))
        (else (count name (cdr s)))))

(define (tally names)
  (if (null? names) 
    nil
    (cons 
      (cons (car names) (count (car names) names)) 
      (tally (filter (lambda (x) (not (eq? x (car names)))) (cdr names))))))


 