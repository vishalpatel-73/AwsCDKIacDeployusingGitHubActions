using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WKTAAE.DPU.Allocation.Contracts.Dtos.StatementJSON.AH
{
    public partial class Statement
    {
        public virtual Ulid Id { get; set; }
        public virtual string FileType { get; set; }
        public virtual Int64 StatementNumber { get; set; }
        public virtual Int64 PaperStatementNumber { get; set; }
        public virtual BankAccount? BankAccount { get; set; }
        public virtual BalanceDetail InitialBalance { get; set; }
        public virtual BalanceDetail FinalBalance { get; set; }
        public virtual string ExtensionZone { get; set; }
        public virtual List<Movement> Movements { get; set; }
    }

    public partial class BankAccount
    {
        public virtual string AccountNumber { get; set; }
        public virtual string CurrencyCode { get; set; }
    }

    public partial class BalanceDetail
    {
        public virtual DateTime BalanceDate { get; set; }
        public virtual bool IsNegative { get; set; }
        public virtual double Value { get; set; }
    }

    public partial class Movement
    {
        public virtual Ulid Id { get; set; }
        public virtual Int64 SequenceNumber { get; set; }
        public virtual DateTime Date { get; set; }
        public virtual Amount ForeignAmount { get; set; }
        public virtual Amount Amount { get; set; }
        public virtual string BookingTarget { get; set; }
        public virtual string TransactionCodes { get; set; }
        public virtual List<MovementDetail> Details { get; set; }
        public virtual string Type { get; set; }
    }

    public partial class Amount
    {
        public virtual string CurrencyCode { get; set; }
        public virtual bool IsNegative { get; set; }
        public virtual double Value { get; set; }
    }

    public partial class MovementDetail
    {
        public virtual Ulid Id { get; set; }
        public virtual Int64 DetailNr { get; set; }
        public virtual DateTime Date { get; set; }
        public virtual Amount Amount { get; set; }
        public virtual string BookingTarget { get; set; }
        public virtual string TransactionCodes { get; set; }
    }
}
