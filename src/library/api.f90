subroutine pcg(a, b, x, tol, maxit, neq, fprint)
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
    call pcg_(a, b, x, tol, maxit, neq, fprint)

end subroutine pcg
