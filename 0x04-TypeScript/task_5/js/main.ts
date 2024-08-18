interface MajorCredits {
  credits: number;
  brand: string;
}

interface MinorCredits {
  credits: number;
  brand: string;
}

interface SumCredits {
  (
    subject1: MajorCredits | MinorCredits,
    subject2: MajorCredits | MinorCredits,
  ): number;
}

const sumMajorCredits: SumCredits = (
  subject1: MajorCredits,
  subject2: MinorCredits,
): number => {
  return subject1.credits + subject2.credits;
};

const sumMinorCredits: SumCredits = (
  subject1: MajorCredits,
  subject2: MinorCredits,
): number => {
  return subject1.credits + subject2.credits;
};
