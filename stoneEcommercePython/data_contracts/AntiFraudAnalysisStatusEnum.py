from enum import Enum


class AntiFraudAnalysisStatusEnum(Enum):
    PendingFraudAnalysisRequirement = 1,
    FraudAnalysisRequirementSent = 2,
    Approved = 3,
    Reproved = 4,
    PendingManualAnalysis = 5,
    NoTransactionToAnalyse = 6,
    FraudAnalysisWithError = 7