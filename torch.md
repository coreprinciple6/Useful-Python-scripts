```
import uuid
def generate_key(self,id_len=4):
    ids = uuid.uuid4().hex[:id_len]
    return ids
```

```
cv2.imwrite(folder+'/'+str(self.generate_key(3))+'.jpg', face)
```

### torch squeeze and unsqueeze
"Simply put, unsqueeze() "adds" a superficial 1 dimension to tensor (at the specified dimension), while squeeze removes all superficial 1 dimensions from tensor." [link](https://stackoverflow.com/questions/61598771/pytorch-squeeze-and-unsqueeze)

```
# 3 channels, 32 width, 32 height
tensor = torch.randn(3, 32, 32)
# 1 batch, 3 channels, 32 width, 32 height
res = tensor.unsqueeze(dim=0)
print(res)  #(1,3,32,32)
# using -1 as dim means the last item or dimension

```
### torch.view
```
# here removed 1st adn 2nd dim then reshaped tensor to one single line/dim
embed = embed.squeeze(0).squeeze(1).view(-1,512)
```

### torch.concat vs stack
```
concat adds tensors while maintaining the same dimensions. stack adds tensors in a new dimension
res = torch.cat(x1,x2,-1)  #-1 means x2 is added after x1

```