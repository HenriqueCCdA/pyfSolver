subroutine matvec_coo(a, row, col, x, y, nnz, n)
    implicit none
    integer, intent(in) :: nnz, n
    integer, dimension(nnz), intent(in) :: row, col
    real(kind=8), dimension(nnz), intent(in) :: a
    real(kind=8), dimension(n), intent(in) :: x
    real(kind=8), dimension(n), intent(inout) :: y
    integer :: i, irow, icol
    y = 0.d0
    do i = 1, nnz
        irow = row(i) + 1
        icol = col(i) + 1
        y(irow) = y(irow) + a(i) * x(icol)
    enddo
end subroutine matvec_coo
