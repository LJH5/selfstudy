package com.ss.hello;

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/LIfeCycleTest")
public class LIfeCycleTest extends HttpServlet {
	private static final long serialVersionUID = 1L;

    public LIfeCycleTest() {
        super();
        System.out.println("객체를 생성합니다.");
    }

	@Override
	public void destroy() { 
		// TODO Auto-generated method stub
		super.destroy();
		System.out.println("객체를 제거합니다.");
	}

	@Override
	public void init() throws ServletException {
		super.init();
		System.out.println("객체를 초기화합니다.");
	}

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		System.out.println("클라이언트 요청 서비스합니다.");
	}


}
