subroutine relax(xc,yc,dist,ierr,maxiter)
implicit none
integer,parameter  :: default_iter
real(8),intent(in) :: dist !constrained distance between neighbours
integer,intent(in),optional ::maxiter
integer,intent(out) :: ierr ! if  success then equals to zero
real(8),intent(inout) ::xc(:,:),yc(:,:)
integer               :: Nx,Ny,i,j,iter
!shape of xc and yc must be same
if (size(xc,1)/=size(yc,1).or.size(xc,2).ne.size(yc,2))
        ierr = 1
        return 
endif

Nx = size(xc,1)
Ny = size(xc,2)
if (.not.present(maxiter)) 
        iter=default_iter !default value of iter
else
        iter=maxiter
endif
do i=2,Nx
   do j=2,Ny
      !relax with left vertex
      call relax_with(i-1,j)
      !relax with top vertex
      call relax_with(i,j-1)
   enddo
enddo

contains
!This is inner subroutine, all variables of relax are
!seen from here
subroutine relax(i1,j1)
implicit none
integer :: i1,j1
real(8) :: dx,dy,k
real(8) :: xm,ym
dx = xc(i,j) - xc(i1,j1)
dy = yc(i,j) - yc(i1,j1)
k = dist/sqrt(dx**2+dy**2)
xm = (xc(i,j) + xc(i1,j1))/2d0
ym = (yc(i,j) + yc(i1,j1))/2d0

xc(i,j) = xm + dx/2*k
yc(i,j) = ym + dy/2*k

xc(i1,j1) = xm - dx/2*k
yc(i1,j1) = ym - dy/2*k
endsubroutine

endsubroutine
