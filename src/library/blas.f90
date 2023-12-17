function dot(x, y, n) result(d)
    implicit none
    integer, intent(in) :: n
    real(kind=8), dimension(n), intent(in) :: x, y
    real(kind=8) :: d
    integer :: i

    d = 0.0d0
    do i = 1, n
        d = d + x(i) * y(i)
    enddo
end function dot

subroutine matvec_(a, x, y, n)
    implicit none
    integer, intent(in) :: n
    real(kind=8), dimension(n), intent(in) :: x
    real(kind=8), dimension(n), intent(inout) :: y
    real(kind=8), dimension(n,n), intent(in) :: a
    integer :: i, j

    y = 0.d0
    do j = 1, n
        do i = 1, n
            y(i) = y(i) + a(i,j) * x(j)
        enddo
    enddo
end subroutine matvec_


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
