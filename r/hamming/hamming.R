hamming <- function(strand1, strand2) {
    if( nchar(strand1) != nchar(strand2) ) stop('strand lengths do not match')

    len <- nchar(strand1)
    res <- 0

    for ( v in 1:len ) {
        if ( substr(strand1, v, v) != substr(strand2, v, v) ) res = res+1
    }

    return(res)
}
