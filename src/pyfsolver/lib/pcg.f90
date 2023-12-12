subroutine pcg_(a, b, x, tol, maxit, neq, fprint)
    implicit none
    integer, intent(in) :: neq
    !
    real(8), dimension(neq), intent(in) :: b
    real(8), dimension(neq, neq), intent(in) :: a
    real(8), dimension(neq), intent(inout) :: x
    real(8), intent(in) :: tol
    integer, intent(in) :: maxit
    logical, intent(in) :: fprint
    !
    real(8), dimension(:), allocatable :: m, z, r, p
    integer :: i, j
    real(8) :: d, dot, norm_b, conv, alpha, beta, di, xKx, norm_x
    external dot

    !  arranjos auxiliares
    allocate(m(neq), z(neq), r(neq), p(neq))

    ! Precondicionador
    do i=1, neq
        m(i) = 1.d0 / a(i, i)
    enddo

    ! chute inicial
    x = 0.d0

    ! conv = tol * | (M-1) b |m = tol (b, M(-1)b)
    z = m * b
    d = dot(b, z, neq)
    norm_b = dsqrt(dabs(d))
    conv = tol * norm_b

    ! ||b||
    norm_b = dsqrt(dot(b, b, neq))

    call matvec(a, x, z, neq)

    ! r = b - Ax0
    r = b - z

    ! z0 = M(-1)r0
    z = m * r
    p = z
    ! ( r(0),z(0) ) = ( r(0), (M-1)r0 )
    d = dot(r, z, neq)

    do j = 1, maxit

        ! z = Ap(j)
        call matvec(a, p, z, neq)

        ! alpha =( r(j),z(j) ) / ( Ap(j), p(j) ))
        alpha = d / dot(p, z, neq)

        do i=1, neq
            ! x(j+1) = x(j) + alpha*p
            x(i) = x(i) + alpha * p(i)
            ! r(j+1) = r(j) - alpha*Ap*/
            r(i) = r(i) - alpha * z(i)
        enddo

        ! z  = (M-1)r0
        z = m * r

        ! (r(j + 1), (M - 1)r(j + 1)) = (r(j + 1), z)
        di = dot(r, z, neq)
        ! beta = ( r(j+1),(M-1)r(j+1) ) / ( r(j),r(j) )
        beta = di / d

        ! p(j+1) = (M-1)r(j+1) + beta*p(j) = z + beta*p(j)
        do i=1, neq
            p(i) = z(i) + beta * p(i)
        enddo

        d = di;
        if (dsqrt(dabs(d)) < conv) exit;

    enddo

    ! Energy norm:  x*Kx
    call matvec(a, x, z, neq);
    ! norma de energia = xTAx
    xKx = dot( x, z, nEq);

    ! norm = || x ||
    norm_x = sqrt(dot(x, x, neq));

10  format('(PCG) solver:'/&
        ,'Solver tol           = ',d20.6/&
        ,'Number of equations  = ',i20/&
        ,'Number of iterations = ',i20/&
        ,'| xKx |              = ',d20.10/&
        ,'| x |                = ',d20.10&
    )

    if (fprint) then
        print 10, tol, neq, j, xKx, norm_x
    endif

    ! free
    deallocate(m, z, r, p)

end subroutine pcg_
