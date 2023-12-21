subroutine pcg(a, row, col, b, x, tol, maxit, nnz, neq, fprint)
   implicit none
   integer, intent(in) :: nnz, neq
   !
   integer, dimension(nnz), intent(in) :: row, col
   real(8), dimension(nnz), intent(in) :: a
   real(8), dimension(neq), intent(in) :: b
   real(8), dimension(neq), intent(inout) :: x
   real(8), intent(in) :: tol
   integer, intent(in) :: maxit
   logical, intent(in) :: fprint
   !
   call pcg_(a, row, col, b, x, tol, maxit, nnz, neq, fprint)

end subroutine pcg

subroutine matvec(a, row, col, x, y, nnz, n)
   implicit none
   integer, intent(in) :: nnz, n
   integer(kind=4), dimension(nnz), intent(in) :: row, col
   real(kind=8), dimension(nnz), intent(in) :: a
   real(kind=8), dimension(n), intent(in) :: x
   real(kind=8), dimension(n), intent(inout) :: y
   call matvec_coo(a, row, col, x, y)
end subroutine matvec
