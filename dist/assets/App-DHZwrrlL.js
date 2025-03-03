import{j as r,r as i,u as d,L as f,O as g}from"./index-Bz09jjKG.js";function b(){return r.jsx("div",{className:"z-50 col-span-3 grid size-full grid-cols-[55px,_180px,_1fr] bg-main",children:r.jsx("div",{className:"flex items-center justify-center text-[20px] font-bold text-light",children:"hwon-da.githu.io"})})}/**
 * @license lucide-react v0.464.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */const v=t=>t.replace(/([a-z0-9])([A-Z])/g,"$1-$2").toLowerCase(),x=(...t)=>t.filter((e,s,a)=>!!e&&e.trim()!==""&&a.indexOf(e)===s).join(" ").trim();/**
 * @license lucide-react v0.464.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */var w={xmlns:"http://www.w3.org/2000/svg",width:24,height:24,viewBox:"0 0 24 24",fill:"none",stroke:"currentColor",strokeWidth:2,strokeLinecap:"round",strokeLinejoin:"round"};/**
 * @license lucide-react v0.464.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */const j=i.forwardRef(({color:t="currentColor",size:e=24,strokeWidth:s=2,absoluteStrokeWidth:a,className:n="",children:o,iconNode:c,...l},h)=>i.createElement("svg",{ref:h,...w,width:e,height:e,stroke:t,strokeWidth:a?Number(s)*24/Number(e):s,className:x("lucide",n),...l},[...c.map(([m,p])=>i.createElement(m,p)),...Array.isArray(o)?o:[o]]));/**
 * @license lucide-react v0.464.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */const u=(t,e)=>{const s=i.forwardRef(({className:a,...n},o)=>i.createElement(j,{ref:o,iconNode:e,className:x(`lucide-${v(t)}`,a),...n}));return s.displayName=`${t}`,s};/**
 * @license lucide-react v0.464.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */const y=u("Map",[["path",{d:"M14.106 5.553a2 2 0 0 0 1.788 0l3.659-1.83A1 1 0 0 1 21 4.619v12.764a1 1 0 0 1-.553.894l-4.553 2.277a2 2 0 0 1-1.788 0l-4.212-2.106a2 2 0 0 0-1.788 0l-3.659 1.83A1 1 0 0 1 3 19.381V6.618a1 1 0 0 1 .553-.894l4.553-2.277a2 2 0 0 1 1.788 0z",key:"169xi5"}],["path",{d:"M15 5.764v15",key:"1pn4in"}],["path",{d:"M9 3.236v15",key:"1uimfh"}]]);/**
 * @license lucide-react v0.464.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */const k=u("SquareUserRound",[["path",{d:"M18 21a6 6 0 0 0-12 0",key:"kaz2du"}],["circle",{cx:"12",cy:"11",r:"4",key:"1gt34v"}],["rect",{width:"18",height:"18",x:"3",y:"3",rx:"2",key:"afitv7"}]]);function N(){const t=[{path:"/",icon:k,label:"관리자"},{path:"/second",icon:y,label:"second"}],e=d("/"),s=d("/second"),a=[e,s];return r.jsx("div",{className:"box-border flex size-full flex-col border-t border-gray7 bg-main",children:t.map(({path:n,icon:o,label:c},l)=>r.jsxs(f,{to:n,className:"box-border flex h-[65px] w-full flex-col items-center justify-center border-b border-gray7"+(a[l]?" bg-blue text-light":""),children:[r.jsx(o,{className:"text-light",width:"20",height:"20"}),r.jsx("div",{className:"m-[2px] text-[12px] font-bold text-light",children:c})]},n))})}function M(){return r.jsxs("div",{id:"app",className:"relative grid h-screen w-screen grid-cols-[60px,_1fr] grid-rows-[55px,_1fr] overflow-hidden",children:[r.jsx(b,{}),r.jsx(N,{}),r.jsx(g,{})]})}export{M as default};
