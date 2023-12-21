program test_matec
   implicit none
   real(kind=8), parameter :: EPS = 1.d-06
   real(kind=8), dimension(9) :: a
   real(kind=8), dimension(3) :: x, y, expected
   integer(kind=4), dimension(9) :: row, col
   integer :: i

   a = [1.0, 0.2, 0.3, 6.0, 0.0, 1.0, 0.2, 0.3, 0.0]
   row = [0, 0, 0, 1, 1, 2, 1, 2, 2]
   col = [0, 1, 2, 1, 2, 2, 0, 0, 1]
   x = [2.0, 2.0, 3.0]
   y = 0.0

   call matvec_coo(a, row, col, x, y, 9, 3)

   expected = [3.3, 12.4, 3.6]

   do i = 1, 3
      if (.NOT. (dabs(y(1) - expected(1)) < EPS)) then
         print *, "got:", y(i), "expected:", expected(i)
         error stop 1
      end if
   end do
end program test_matec
