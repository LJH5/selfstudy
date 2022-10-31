package java01.intro;

public class Intro03_PrintTest {

	public static void main(String[] args) {
		//이어 쓰기
		System.out.print("Hello world");
		
		//줄바꿈
		System.out.println("Hello world!!!");
		System.out.print("Hello world\n");
		
		//기호를 출력
		System.out.println("\\");
		System.out.println("\"");
		
		System.out.printf("%d \n", 10); //10진수
		System.out.printf("%o \n", 10); //8진수
		System.out.printf("%X \n", 10); //16진수(대문자)
		System.out.printf("%x \n", 10); //16진수(소문자)
		
		System.out.printf("%4d\n", 10); //4칸 확보 후 오른쪽 부터
		System.out.printf("%-4d\n", 10); //4칸 확보 후 왼쪽 부터
		System.out.printf("%04d\n", 10); //4칸 확보 후 오른쪽 부터(빈칸은 0으로)
		
		System.out.printf("f\n", 10,1);	//실수
		System.out.printf(".2f\n", 10.10); //실수(소수점 둘째자리까지)
		
		System.out.printf("%s\n", "abc"); //문자열
		System.out.printf("%c\n", 'a'); //문자
		
		System.out.printf("안녕하세요. 저는  %s입니다. 저는 %d살 입니다", "홍길동", 27);
		
	}

}
