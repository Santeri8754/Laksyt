
const id = document.querySelector('#target');

 const i = document.createElement('li');
  const i2 = document.createElement('li');
  const i3 = document.createElement('li');
 const t = document.createTextNode('First item');
 const t2 = document.createTextNode('Second item');
 const t3 = document.createTextNode('Third item');


 i.appendChild(t)
i2.appendChild(t2)
i3.appendChild(t3)

id.appendChild(i);
 id.appendChild(i2);
 id.appendChild(i3);