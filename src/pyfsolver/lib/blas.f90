function dot(x, y, n) result(d)
    implicit none
    real(kind=8), dimension(n), intent(in) :: x, y
    integer, intent(in) :: n
    real(kind=8) :: d
    integer :: i

    d = 0.0d0
    do i = 1, n
        d = d + x(i) * y(i)
    enddo
end function dot

subroutine matvec(a, x, y, n)
    implicit none
    real(kind=8), dimension(n), intent(in) :: x
    real(kind=8), dimension(n), intent(inout) :: y
    real(kind=8), dimension(n,n), intent(in) :: a
    integer, intent(in) :: n
    integer :: i, j

    y = 0.d0
    do j = 1, n
        do i = 1, n
            y(i) = y(i) + a(i,j) * x(j)
        enddo
    enddo
end subroutine matvec
