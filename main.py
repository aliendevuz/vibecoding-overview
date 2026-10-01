"""
Python dasturlash tili bo'yicha amaliy namuna kod.
Mavzu: Talabalar va ularning baholarini boshqarish tizimi.
Bu namunada quyidagilar qamrab olingan:
1. Funksiyalar va type hint'lar
2. Ro'yxat (list) va lug'at (dict) bilan ishlash
3. List comprehension
4. Oddiy sinf (Class / OOP)
"""

from typing import List, Dict


class Student:
    """Talaba ma'lumotlarini saqlovchi va o'rtacha ballni hisoblovchi sinf."""

    def __init__(self, name: str, grades: List[int]):
        self.name = name
        self.grades = grades

    def get_average(self) -> float:
        """Talabaning o'rtacha bahosini hisoblaydi."""
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def is_passed(self, passing_grade: float = 60.0) -> bool:
        """Talaba imtihondan o'tgan yoki o'tmaganligini aniqlaydi."""
        return self.get_average() >= passing_grade


def analyze_students(students: List[Student]) -> Dict[str, any]:
    """Talabalar ro'yxatini tahlil qiladi va umumiy hisobot tayyorlaydi."""
    passed_students = [s.name for s in students if s.is_passed()]
    failed_students = [s.name for s in students if not s.is_passed()]

    total_avg = (
        sum(s.get_average() for s in students) / len(students)
        if students
        else 0.0
    )

    return {
        "jami_talabalar": len(students),
        "o'rtacha_ball": round(total_avg, 2),
        "o'tganlar": passed_students,
        "yiqilganlar": failed_students,
    }


def main():
    # 1. Talabalar ma'lumotlarini yaratish
    students = [
        Student("Sevara", [85, 90, 92, 88]),
        Student("Jasur", [55, 60, 48, 58]),
        Student("Dilshod", [70, 75, 80, 68]),
        Student("Madina", [95, 98, 100, 94]),
    ]

    print("=== TALABALAR NATIJALARI ===")
    for student in students:
        avg = student.get_average()
        status = "[O'tdi]" if student.is_passed() else "[Yiqildi]"
        print(f"- {student.name:10}: O'rtacha baho = {avg:.1f} | {status}")

    # 2. Umumiy tahlil
    stats = analyze_students(students)

    print("\n=== UMUMIY STATISTIKA ===")
    print(f"Jami talabalar soni : {stats['jami_talabalar']}")
    print(f"Guruh o'rtacha bali : {stats['o\'rtacha_ball']}")
    print(f"Muvaffaqiyatli       : {', '.join(stats['o\'tganlar'])}")
    print(f"Qayta topshirish     : {', '.join(stats['yiqilganlar'])}")


if __name__ == "__main__":
    main()
