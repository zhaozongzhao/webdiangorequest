"""
1.全局路由和子路由的作用以及路由匹配规则

  答：
   作用： 告诉Django对客户端发过来的某个URL应该调用执行哪一段逻辑代码
   规则：
   1. 从上往下依次查找,如果django会导入和调用path函数第二个参数指定的视图获取去子路由中匹配
   2，如果匹配不上会抛出一个404（默认404页面，状态404）
   3. 列表中的一个元素，就代表一条路由

2.搭建Django工程
   已完成，见附件

3，前后端分离和不分离开发模式的区别:
    区别：
    1，前后端不分离页面由后端控制，耦合度比较高
    2，前后端分离，后端仅返回前端所需的数据，不再渲染HTML页面，不再控制前端的效果。至于前端用户看到什么效果，
    从后端请求的数据如何加载到前端中，都由前端自己决定，在前后端分离的应用模式中 ，前端与后端的耦合度相对较低

"""