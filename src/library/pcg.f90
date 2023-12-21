subroutine precond_diag(m, a, row, col, nnz)
   implicit none
   integer, intent(in) :: nnz
   real(kind=8), dimension(nnz), intent(in) :: a
   integer, dimension(nnz), intent(in) :: row, col
   real(kind=8), dimension(nnz), intent(inout) :: m
   integer i
   do i = 1, nnz
      if (row(i) == col(i)) then
         m(row(i) + 1) = 1.d0/a(i)
      end if
   end do
end subroutine precond_diag

subroutine pcg_(a, row, col, b, x, tol, maxit, nnz, neq, fprint)
   implicit none
   integer, intent(in) :: neq, nnz
   !
   integer, dimension(nnz), intent(in) :: row, col
   real(8), dimension(nnz), intent(in) :: a
   real(8), dimension(neq), intent(in) :: b
   real(8), dimension(neq), intent(inout) :: x
   real(8), intent(in) :: tol
   integer, intent(in) :: maxit
   logical, intent(in) :: fprint
   !
   real(8), dimension(:), allocatable :: m, z, r, p
   integer :: j
   real(8) :: d, norm_b, conv, alpha, beta, di, xKx, norm_x
   external matvec_coo

   !  arranjos auxiliares
   allocate (m(neq), z(neq), r(neq), p(neq))

   ! Precondicionador
   call precond_diag(m, a, row, col, nnz)

   ! chute inicial
   x = 0.d0

   ! conv = tol * | (M-1) b |m = tol (b, M(-1)b)
   z = m*b
   d = dot_product(b, z)
   norm_b = dsqrt(dabs(d))
   conv = tol*norm_b

   ! ||b||
   norm_b = dsqrt(dot_product(b, b))

   call matvec_coo(a, row, col, x, z, nnz, neq)

   ! r = b - Ax0
   r = b - z

   ! z0 = M(-1)r0
   z = m*r
   p = z
   ! ( r(0),z(0) ) = ( r(0), (M-1)r0 )
   d = dot_product(r, z)

   do j = 1, maxit

      ! z = Ap(j)
      call matvec_coo(a, row, col, p, z, nnz, neq)

      ! alpha =( r(j),z(j) ) / ( Ap(j), p(j) ))
      alpha = d/dot_product(p, z)

      ! x(j+1) = x(j) + alpha*p
      x = x + alpha*p

      ! r(j+1) = r(j) - alpha*Ap*/
      r = r - alpha*z

      ! z  = (M-1)r0
      z = m*r

      ! (r(j + 1), (M - 1)r(j + 1)) = (r(j + 1), z)
      di = dot_product(r, z)
      ! beta = ( r(j+1),(M-1)r(j+1) ) / ( r(j),r(j) )
      beta = di/d

      ! p(j+1) = (M-1)r(j+1) + beta*p(j) = z + beta*p(j)
      p = z + beta*p

      d = di
      if (dsqrt(dabs(d)) < conv) exit
   end do

   ! norma de energia = xTAx
   call matvec_coo(a, row, col, x, z, nnz, neq)
   xKx = dot_product(x, z)
   ! norm = || x ||
   norm_x = sqrt(dot_product(x, x))
10 format('(PCG) solver:'/ &
          , 'Solver tol           = ', E20.6/ &
          , 'Number of equations  = ', i20/ &
          , 'Number of iterations = ', i20/ &
          , '|| xKx ||            = ', E20.10/ &
          , '|| x ||              = ', E20.10/ &
          , '|| b ||              = ', E20.10 &
          )

   if (fprint) then
      print 10, tol, neq, j, xKx, norm_x, norm_b
   end if

   ! free
   deallocate (m, z, r, p)

end subroutine pcg_
