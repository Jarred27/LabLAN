img=imread('hello world.png');
logical=img(:,:,1)'==0;
idx=find(logical==1);

array=zeros(1,60*60);
for i=idx
    array(i)=mod(i,60)./30;
end
array=array-1;
createTFW(array,'hello world.tfw')