package com.ss.hello;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/hello")
public class HelloServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;

	private String name;
	
	public void init() {
		name = "홍길동";
	}
	
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
//		1. data get
		
//		2. logic
		
//		3. response page ==> html
		PrintWriter out = response.getWriter();
		out.println("<html>");
		out.println("	<body>");
		out.println("		<h2>Hello Servlet!!!</h2>");
		out.println("		<h2>" + name +"님 안녕하세요!!!</h2>");
		out.println("	</body>");
		out.println("</html>");
	}

}
