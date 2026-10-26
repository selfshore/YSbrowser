(()=>{
  const root=document.documentElement;
  const store=(key,value)=>{try{localStorage.setItem(key,value)}catch{}};
  try{root.dataset.theme=localStorage.getItem('ys-doc-theme')||'light';if(localStorage.getItem('ys-doc-large')==='1')document.body.classList.add('large-text')}catch{}
  document.querySelector('#theme-toggle').addEventListener('click',()=>{root.dataset.theme=root.dataset.theme==='dark'?'light':'dark';store('ys-doc-theme',root.dataset.theme)});
  document.querySelector('#font-toggle').addEventListener('click',()=>{document.body.classList.toggle('large-text');store('ys-doc-large',document.body.classList.contains('large-text')?'1':'0')});
  document.querySelector('#menu-toggle').addEventListener('click',()=>document.body.classList.toggle('nav-open'));
  document.querySelector('main').addEventListener('click',()=>document.body.classList.remove('nav-open'));
  document.querySelectorAll('.copy-code').forEach(button=>button.addEventListener('click',async()=>{
    const code=button.closest('.code-block').querySelector('code').textContent;
    let copied=false;
    try{await navigator.clipboard.writeText(code);copied=true}catch{
      const field=document.createElement('textarea');field.value=code;field.style.position='fixed';field.style.left='-9999px';document.body.append(field);field.select();copied=document.execCommand('copy');field.remove();
    }
    button.textContent=copied?'已复制':'请手动复制';button.dataset.copied=String(copied);
    setTimeout(()=>button.textContent='复制代码',1600);
  }));
  const dialog=document.querySelector('#search-dialog'),input=document.querySelector('#search-input'),results=document.querySelector('#search-results');
  const openSearch=()=>{if(!dialog.open)dialog.showModal();input.focus()};
  document.querySelector('#search-open').addEventListener('click',openSearch);
  document.querySelector('#search-close').addEventListener('click',()=>dialog.close());
  dialog.addEventListener('click',event=>{if(event.target===dialog)dialog.close()});
  document.addEventListener('keydown',event=>{if((event.ctrlKey||event.metaKey)&&event.key.toLowerCase()==='k'){event.preventDefault();openSearch()}});
  let timer;
  input.addEventListener('input',()=>{clearTimeout(timer);timer=setTimeout(search,100)});
  function search(){
    const terms=input.value.trim().toLowerCase().split(/\s+/).filter(Boolean);results.replaceChildren();
    if(!terms.length){const p=document.createElement('div');p.className='search-message';p.textContent='搜索 API、参数或问题，例如 drag_element、hold_ms、代理。';results.append(p);return}
    const hits=(window.DOC_SEARCH||[]).map(item=>{
      const title=(item.page+' '+item.title).toLowerCase(),text=item.text.toLowerCase();
      if(!terms.every(term=>title.includes(term)||text.includes(term)))return null;
      return {item,score:terms.reduce((score,term)=>score+(item.title.toLowerCase()===term?30:title.includes(term)?10:1),0)};
    }).filter(Boolean).sort((a,b)=>b.score-a.score).slice(0,40);
    if(!hits.length){const p=document.createElement('div');p.className='search-message';p.textContent='没有匹配结果，试试方法名或更短的关键词。';results.append(p)}
    for(const {item} of hits){
      const a=document.createElement('a');a.className='search-result';a.href=(root.dataset.docRoot||'')+item.url;
      const title=document.createElement('strong');title.textContent=item.title;
      const context=document.createElement('small');context.textContent=item.page;
      const excerpt=document.createElement('small');const low=item.text.toLowerCase();let at=low.indexOf(terms[0]);at=Math.max(0,at-45);excerpt.textContent=item.text.slice(at,at+150);
      a.append(title,context,excerpt);a.addEventListener('click',()=>dialog.close());results.append(a);
    }
  }
  const toc=[...document.querySelectorAll('.toc a')];
  if('IntersectionObserver' in window){const observer=new IntersectionObserver(entries=>{for(const e of entries)if(e.isIntersecting){toc.forEach(a=>a.classList.toggle('active',decodeURIComponent(a.hash.slice(1))===e.target.id))}},{rootMargin:'-12% 0px -70% 0px'});document.querySelectorAll('main h2,main h3').forEach(h=>observer.observe(h))}
  search();
})();
