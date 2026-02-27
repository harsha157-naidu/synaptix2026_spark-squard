// Function to calculate match score
function calculateMatch() {

    // 1️⃣ Get Candidate Skill Values
    const skills = {
        programming: parseFloat(document.getElementById("prog").value),
        communication: parseFloat(document.getElementById("comm").value),
        problemSolving: parseFloat(document.getElementById("problem").value),
        teamwork: parseFloat(document.getElementById("team").value)
    };

    // 2️⃣ Get Project Requirement Weights
    const weights = {
        programming: parseFloat(document.getElementById("w_prog").value),
        communication: parseFloat(document.getElementById("w_comm").value),
        problemSolving: parseFloat(document.getElementById("w_problem").value),
        teamwork: parseFloat(document.getElementById("w_team").value)
    };

    // 3️⃣ Check if Fairness Adjustment is Enabled
    const fairnessEnabled = document.getElementById("fairness").checked;

    // 4️⃣ Calculate Total Weight
    const totalWeight =
        weights.programming +
        weights.communication +
        weights.problemSolving +
        weights.teamwork;

    // 5️⃣ Calculate Weighted Score
    let matchScore =
        (skills.programming * weights.programming +
         skills.communication * weights.communication +
         skills.problemSolving * weights.problemSolving +
         skills.teamwork * weights.teamwork) / totalWeight;

    // 6️⃣ Apply Fairness Adjustment (if enabled)
    if (fairnessEnabled) {
        matchScore = matchScore * 1.05;  // 5% fairness boost
    }

    // 7️⃣ Format Score to 2 Decimal Places
    matchScore = matchScore.toFixed(2);

    // 8️⃣ Display Ranking
    document.getElementById("ranking").innerHTML = `
        <div class="candidate-item" onclick="showExplanation(${matchScore})">
            Candidate A
            <span class="score-badge">${matchScore}</span>
        </div>
    `;
}


// Function to Show Explanation
function showExplanation(score) {

    const fairnessStatus =
        document.getElementById("fairness").checked
            ? "Enabled ⚖️"
            : "Disabled";

    document.getElementById("explain").innerHTML = `
        <div class="explanation">
            <strong>📊 Match Score Breakdown</strong><br><br>

            ✔ Weighted competency scoring applied<br>
            ✔ Skills mapped to project requirement importance<br>
            ✔ Fairness Adjustment: ${fairnessStatus}<br><br>

            ⭐ Final Match Score: <b>${score}</b><br><br>

            This ranking is transparent and based purely on 
            weighted evaluation instead of keyword matching.
        </div>
    `;
}