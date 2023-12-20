program test_pcg
    implicit none
    real(kind=8), parameter :: EPS = 1.d-06
    real(kind=8), dimension(9) :: a
    real(kind=8), dimension(3) :: b, x, expected
    integer(kind=4), dimension(9) :: row, col
    integer :: i

    a = [1.0, 0.2, 0.3, 6.0, 0.0, 1.0, 0.2, 0.3, 0.0]
    row = [0, 0, 0, 1, 1, 2, 1, 2, 2]
    col = [0, 1, 2, 1, 2, 2, 0, 0, 1]
    b = [2.0, 6.0, 1.0]

    call pcg_(a, row, col, b, x, 1.d-11, 100, 9, 3, .false.)

    expected = [1.6605166051660516,  0.9446494464944649, 0.5018450184501844]

    do i = 1, 3
        if(.NOT. (dabs(x(1)-expected(1)) < EPS)) then
            print*, "got:", x(i), "expected:", expected(i)
            error stop 1
        endif
    enddo
end program test_pcg
