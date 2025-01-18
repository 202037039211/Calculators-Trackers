// Function to calculate the average of scores
function getAverage(scores) {
  let sum = 0;

  // Loop through the scores and sum them up
  for (const score of scores) {
    sum += score;
  }

  // Return the average score
  return sum / scores.length;
}

// Function to determine the grade based on the score
function getGrade(score) {
  if (score === 100) {
    return "A++"; // Top grade
  } else if (score >= 90) {
    return "A"; // Excellent grade
  } else if (score >= 80) {
    return "B"; // Good grade
  } else if (score >= 70) {
    return "C"; // Average grade
  } else if (score >= 60) {
    return "D"; // Below average grade
  } else {
    return "F"; // Fail
  }
}

// Function to check if the score is a passing grade
function hasPassingGrade(score) {
  return getGrade(score) !== "F"; // If the grade is not 'F', it's a passing grade
}

// Function to generate a message with class average and student's grade
function studentMsg(totalScores, studentScore) {
  // Calculate the class average
  const classAverage = getAverage(totalScores);
  
  // Get the student's grade based on their score
  const studentGrade = getGrade(studentScore);
  
  // Check if the student passed or failed
  const passOrFail = hasPassingGrade(studentScore) ? "passed" : "failed";
  
  // Return a message with the class average, student's grade, and pass/fail status
  return `Class average: ${classAverage.toFixed(1)}. Your grade: ${studentGrade}. You ${passOrFail} the course.`;
}

// Example usage:
console.log(studentMsg([92, 88, 12, 77, 57, 100, 67, 38, 97, 89], 37));
// Output: Class average: 71.7. Your grade: F. You failed the course.
